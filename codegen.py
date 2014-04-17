# -----------------------------------------------------------------------------
# codegen.py
#
# Code Generation
# -----------------------------------------------------------------------------
from datatypes import *
from ast import *
import sys
import block
import adalex
import adaparse
import os
import typecheck


counter = 0
endcounter = 0
whileCounter = 0
whilePointer = 0
numchar = 0
filepath = None
env = None


class Stack:
    def __init__(self):
        self.env = []
        #self.activationRecord = ActivationRecord()
    def push(self, x):
        self.env += [x]   
    def pop(self):
        if len(self.env) == 0:
            raise RuntimeError()
        val = self.env[-1]
        self.env = self.env[0:-1]
        return val
    def peek(self):
        #print "{", self.env, "}"
        return self.env[-1]


class ActivationRecord:
    def __init__(self):
        self.rec =[]
        self.type = {}
        self.size = {'INTEGER': 4, 'FLOAT':4, 'CHARACTER':4}
    def addSize(self, tp, sz):
        self.size[tp] = sz
    def store(self, Name, Type):
        self.rec += [Name]
        self.type[Name] = Type
    def index(self, name):
        for i in xrange(len(self.rec)):
            if self.rec[i] == name: return i
        return -1
    def length(self):
        return len(self.rec)

    def getType(self, name):
        if name in self.type:
            return self.type[name]
        return None
    def sizeOf(self, name):
        t = self.getType(name)
        if t != None:
            return self.size[t]
        return None

    def get(self, Name=None):
        if Name == None:
            count = 0
            for i in xrange(len(self.rec)):
                count += self.size[self.type[self.rec[i]]]
            return count
        count = 0
        for i in xrange(len(self.rec)):            
            if self.rec[i] == Name: break
            count += self.size[self.type[self.rec[i]]]
                #print self.rec[i], " --hghg",self.size[self.type[self.rec[i]]]
        return count
    def remove(self):
        '''Removes the last element'''
        last = self.rec[-1]
        self.rec = self.rec[0:-1] 
        self.type.pop(last)   



                
activationStack = Stack()
class GenerateCode():


    program = ''
    def new_temp(self,type):
        name = "%s_%d" % (type.name,self.temp_count)
        self.temp_count += 1
        return name

    def visit_goal_symbol(self,node):
        self.code=''
        self.program = self.code
        self.temp_count = 0
        self.visit(node.compilation)
        self.code=node.compilation.code+'li $v0 10\nsyscall\n'
        program = self.code

    def visit_compilation(self,node):
        #print node.program
        node.code=''
        for comp_unit in node.comp_unit :
            #if isinstance(progra,FuncStatement):
            self.visit(comp_unit)
            node.code+=comp_unit.code

    def visit_FuncStatement(self,node):
        global filepath
        fs, ld = filepath.rfind('/'), filepath.rfind('.')
        name = filepath[fs+1:ld]
        if name.upper()==node.name:
            node.code='.data\nspace: .asciiz "\\n"\nerrmsg: .asciiz "Index out of bounds\\n"\n.text\n.globl main\nmain:\n'
        else:
            node.code ='.text\n'
        node.code+=node.name+':\n'
        #node.code='.data\n'
        ar = ActivationRecord()
        if node.parameters is not None:
            for args in node.parameters.parameters:
                ar.store(args.name, args.typename.name)
            z=len(node.parameters.parameters)
        else :
            z=0
        activationStack.push(ar)
        for vardecl in node.declpart:
            self.visit(vardecl)
            node.code+=vardecl.code
            #ar.store(vardecl.name, vardecl.typename.name)
        z+=len(node.declpart)

        node.code+='move $fp $sp\nsw $ra 0($sp)\naddiu $sp $sp -4\n'
        self.visit(node.statements)
        node.code+=node.statements.code
        node.code+='lw $ra 4($sp)\naddiu $sp $sp 4\n'
        node.code+='lw $fp 4($sp)\naddiu $sp $sp '+str(activationStack.peek().get()+4)+'\njr $ra\n'
        activationStack.pop()

    def visit_VariableDeclaration(self,node):
        ar = activationStack.peek()
        ar.store(node.name, node.typename.name)
        node.code=''
        if node.typename.name == 'ARRAY':
            #print "Inside!", node.length
            arrayLength = node.length.indexconstraint[0][1].right.value-node.length.indexconstraint[0][1].left.value+1
            node.code += "addiu $sp $sp " + str(-4 * (node.length.indexconstraint[0][1].right.value-node.length.indexconstraint[0][1].left.value+1)) + '\n'
            ar.addSize('ARRAY', 4*arrayLength)
            #print "ARRAY Length: ", node.length.indexconstraint.right.value-node.length.indexconstraint.left.value+1
            #print "AR Size: ",activationStack.peek().get()
        else: 
            if node.expr is not None:
                self.visit(node.expr)
                node.code += node.expr.code
                if node.expr.check_type.name=='Character':
                   node.code += 'sb $a0 0($sp)\n'
                else :
                   node.code += 'sw $a0 0($sp)\n' 
            node.code += 'addiu $sp $sp -4\n'        

    def visit_FuncParameter(self,node):
        node.code = node.name+': '
        checktype=node.typename.check_type
        if checktype==IntType:
            node.code+=' .word 1\n'
        elif checktype==CharType:
            node.code+=' .byte 1\n'
        elif checktype==StringType:
            node.code+=' .asciiz ""\n'
        elif checktype==FloatType:
            node.code+=' .float 0.0\n'

    def visit_Literal(self,node):
        #if node.check_type.typename=='FLOAT':
        #    inst = 'li.s $f0 '+str(node.value)+'\n'
        #else: 
        global numchar
        node.code=''
        if hasattr(node,'check_type'):
            if node.check_type==CharType :
                node.code+="li $a0 '"+str(node.value)+"'\n"
            elif node.check_type==FloatType :
                node.code += 'li.s $f12 '+str(node.value)+'\n'
            else :
                node.code += 'li $a0 '+str(node.value)+'\n'
        else :
            node.code += 'li $a0 '+str(node.value)+'\n'

    def visit_Unaryop(self,node):
        checktype=node.check_type.name
        self.visit(node.expr)
        instruction = node.check_type.unary_opcodes[node.op]
        if checktype=='Float':
            inst = instruction+'$f12 $f12\n'
        else:
            inst = instruction+'$a0 $a0\n'
        node.code=inst

    def visit_LoadLocation(self, node):
        checktype = None
        if hasattr(node,'check_type'): checktype=node.check_type
        if checktype == CharType:
            #print "Called !!!!!!!!!!!!"
            inst = 'lw $a0 '+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        elif checktype==StringType:
             inst = 'la $a0 '+node.location.name+'\n'
        elif checktype == FloatType:
            #print "Its a FLOAT"
            inst = 'l.s $f12 '+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        else:
            inst = 'lw $a0 '+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        node.code = inst
        # Save the name of the temporary variable where the value was placed 

    def visit_Binop(self, node):
        if hasattr(node,'check_type'):
            self.visit(node.left)
            node.code = node.left.code
            checktype=node.check_type
            if checktype==FloatType:
                node.code+='s.s $f12 0($sp)\naddiu $sp $sp -4\n'
            else :
                node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
            self.visit(node.right)
            node.code+=node.right.code
            if checktype==FloatType:
                node.code+='l.s $f1 4($sp)\n'
            else :
                node.code+='lw $t1 4($sp)\n'
            instruction = node.check_type.binary_opcodes[node.op]
            if instruction != 'mod':
                if checktype==FloatType:
                    node.code += instruction+' $f12 $f1 $f12\naddiu $sp $sp 4\n'
                else :
                    node.code += instruction+' $a0 $t1 $a0\naddiu $sp $sp 4\n'
            else :
                node.code+='div $a0 $t1 $a0\nmfhi $a0\naddiu $sp $sp 4\n'
        else : 
            self.visit(node.left)
            node.code = node.left.code
            node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
            self.visit(node.right)
            node.code+=node.right.code
            node.code+='lw $t1 4($sp)\n'
            instruction = IntType.binary_opcodes[node.op]
            if instruction != 'mod':
                node.code += instruction+' $a0 $t1 $a0\naddiu $sp $sp 4\n'
            else :
                node.code+='div $a0 $t1 $a0\nmfhi $a0\naddiu $sp $sp 4\n'
 
    def visit_Relop(self, node):
        if hasattr(node,'check_type'):
            self.visit(node.left)
            node.code=node.left.code
            checktype=node.check_type
            if checktype=='Float':
                node.code+='s.s $f12 0($sp)\naddiu $sp $sp -4\n'
            else:
                node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
            self.visit(node.right)
            node.code+=node.right.code
            if checktype==FloatType:
                node.code+='l.s $f1 4($sp)\n'
            else:
                node.code+='lw $t1 4($sp)\n'
            instruction = node.left.check_type.rel_opcodes[node.op]
            if checktype==FloatType:
                inst = instruction+' $f12 $f1 $f12 \naddiu $sp $sp 4\n'
            else:
                inst = instruction+' $a0 $t1 $a0\naddiu $sp $sp 4\n'
            node.code+=inst
        else :
            self.visit(node.left)
            node.code = node.left.code
            node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
            self.visit(node.right)
            node.code+=node.right.code
            node.code+='lw $t1 4($sp)\n'
            instruction = IntType.binary_opcodes[node.op]
            inst = instruction+' $a0 $t1 $a0\naddiu $sp $sp 4\n'
            node.code+=inst


    def visit_ConstDeclaration(self, node):
        self.visit(node.expr)
        if node.scope_level == 0:
            opcode = "newvar_global"
        else:
            opcode = "newvar_local"
        inst = (opcode, node.expr.gen_location, node.name)
        node.code=inst

    def visit_Statements(self,node):
        node.code=''
        for statement in node.statements:
            self.visit(statement)
            node.code+=statement.code

    def visit_AssignmentStatement(self, node):
        self.visit(node.expr)
        node.code=node.expr.code
        inst = ''
        if node.expr.check_type == CharType:
            inst = "sw $a0 "+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        elif node.expr.check_type== FloatType:
            inst = "s.s $f12 "+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        elif node.expr.check_type==IntType:
            inst = "sw $a0 "+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'($fp)\n'
        node.code+=inst

    def visit_ArrayAssignmentStatement(self,node):
        global counter
        self.visit(node.expr)
        node.code = node.expr.code
        node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
        for arg in node.args.arguments:
            self.visit(arg)
            node.code += arg.code
        node.code += 'mul $a0 $a0 4\n'
        counter+=1
        tempcounter=counter
        node.code += 'blt $a0 '+str(activationStack.peek().sizeOf(node.location.name))+' l'+str(tempcounter)+'\n'
        node.code+='la $a0 errmsg\nli $v0 4\nsyscall\nli $v0 10\nsyscall\n'
        node.code+='l'+str(tempcounter)+':\n'
        node.code+='sub $a0 $a0 '+str(activationStack.peek().get() - activationStack.peek().get(node.location.name))+'\n'
        node.code+='mul $a0 $a0 -1\n'
        node.code+='lw $t1 4($sp)\naddiu $sp $sp 4\n'
        node.code+='add $a0 $a0 $fp\nsw $t1 0($a0)\n'
        
    def visit_ExitStatement(self, node):
        node.code=''
        if node.expr != None :
            self.visit(node.expr)
            node.code+=node.expr.code
            if node.name != None :
                node.code+='beq $a0 1 '
            else :
                node.code+='beq $a0 1 '
        else :
            node.code+='j '
        if node.name is not None and node.name.location.name != None :
            node.code+=node.name.location.name+'\n'
        else :
            node.code+='ll'+str(whilePointer)+'\n'

    def visit_ReturnStatement(self,node):
        node.code=''
        if (node.expr != None):
            self.visit(node.expr)
            node.code+=node.expr.code
        node.code+='lw $ra 4($sp)\naddiu $sp $sp 12\nlw $fp 0($sp)\njr $ra\n'

    def visit_GotoStatement(self,node):
        print node
        node.code='b '+node.name.location.name+'\n'

    def visit_ProcCall(self,node):
        node.code='sw $fp 0($sp)\naddiu $sp $sp -4\njal '+node.name.location.name+'\n'

    def visit_FuncCall(self,node):
        node.code=''
        #elif activationStack.peek().index(node.name) < 0:
#changed
        if node.name == 'PUT':
            if isinstance(node.arguments.arguments[0],FuncCall) or node.arguments.arguments[0].location.name != 'NEWLINE':
                checktype = node.arguments.arguments[0].check_type
                self.visit(node.arguments.arguments[0]) 
                node.code+=node.arguments.arguments[0].code
                if checktype==IntType:
                    node.code+='li $v0 1\n'
                elif checktype==CharType:
                    node.code+='li $v0 11\n'
                elif checktype==StringType:
                    node.code+='li $v0 4\n'
                elif checktype==FloatType:
                    node.code+='li $v0 2\n'
                else: node.code+='li $v0 1\n'
                node.code += 'syscall\n'
            else:
                node.code='la $a0 space\nli $v0 4\nsyscall\n'
        elif (hasattr(node,'check_type') and node.check_type==ArrayType) or hasattr(node,'isArray'):# and node.check_type==ArrayType:    #print "Seems an ARRAY!!"
            for argument in node.arguments.arguments:
                self.visit(argument)
                node.code+=argument.code
            node.code += 'mul $a0 $a0 4\n'
            node.code+='sub $a0 $a0 '+str(activationStack.peek().get() - activationStack.peek().get(node.name))+'\n'
            node.code+='mul $a0 $a0 -1\n'
            node.code+='add $a0 $a0 $fp\nlw $a0 0($a0)\n'
        else:
            #print "Fallback to else"
            node.code+='sw $fp 0($sp)\naddiu $sp $sp -4\n'
            for argument in node.arguments.arguments:
                self.visit(argument)
                node.code+=argument.code
                node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
            node.code+='jal '+node.name+'\n'

    def visit_PrintStatement(self, node):
        self.visit(node.expr)
        inst = ("print", node.expr.gen_location)
        node.code=inst

    def visit_IfStatement(self, node):
        #print("visiting %r" % node)
        global counter
        global endcounter
        self.visit(node.expr)
        node.code=node.expr.code
        counter+=1
        tempcounter = counter
        node.code+='beq $a0 0 l'+str(tempcounter)+'\n'
        self.visit(node.truebranch)
        node.code+=node.truebranch.code
        counter+=1
        tempcounter2=counter
        node.code+='j l'+str(tempcounter2)+'\n'
        node.code+='l'+str(tempcounter)+':\n'
        if node.falsebranch is not None:
            self.visit(node.falsebranch)
            node.code+=node.falsebranch.code
        node.code+='l'+str(tempcounter2)+':\n'

    def visit_CaseStatement(self,node):
        global counter
        global endcounter
        self.visit(node.condition)
        node.code=node.condition.code
        node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
        counter+=1
        tempcounter=counter
        if node.alternatives.alternatives is not None:
            for alternative in node.alternatives.alternatives :
                self.visit(alternative)
                node.code+=alternative.code
                node.code+='j l'+str(tempcounter)+'\n'
        node.code+='el'+str(endcounter)+':\nl'+str(tempcounter)+':\n'
        endcounter+=1
        node.code+='addiu $sp $sp 4\n'

    def visit_Alternative(self,node):
        global counter
        global endcounter
        node.code='el'+str(endcounter)+':\n'
        endcounter+=1
        counter+=1
        tempcounter=counter
        for choice in node.choices.choices:
            if choice=='OTHERS':
                node.code+='j l'+str(tempcounter)+'\n'
            else:
                self.visit(choice)
                node.code+=choice.code
                node.code+='lw $t1 4($sp)\nbeq $a0 $t1 l'+str(tempcounter)+'\n'
        node.code+='j el'+str(endcounter)+'\nl'+str(tempcounter)+':\n'
        self.visit(node.statements)
        node.code+=node.statements.code

    def visit_WhileStatement(self,node):
        global counter
        global endcounter
        global whileCounter
        global whilePointer
        whileCounter += 1
        whilePointer = whileCounter 
        tempwhileCounter = whileCounter    
        counter+=1
        tempcounter=counter
        counter+=1
        tempcounter2=counter
        node.code=''
        if isinstance(node.expr,Forloop):
            self.visit(node.expr.name)
            node.code+=node.expr.name.code
            node.code+='lw $t4 8($sp)\nlw $t5 4($sp)\nsw $t4 4($sp)\nsw $t5 8($sp)\naddiu $fp $fp -4\n'
            self.visit(node.expr.discreterange)
            node.code+=node.expr.discreterange.code
            node.code+='lw $a0 8($sp)\nsub $a0 $a0 1\n'
            node.code+="sw $a0 "+str(1 * (activationStack.peek().get() - activationStack.peek().get(node.expr.name.name)))+'($fp)\n'
        node.code+='l'+str(tempcounter)+':\n'
        if isinstance(node.expr,Forloop):
            node.code+='lw $a0 '+str(1 * (activationStack.peek().get() - activationStack.peek().get(node.expr.name.name)))+'($fp)\n'
            node.code+='add $a0 $a0 1\nlw $t4 4($sp)\nbgt $a0 $t4 l'+str(tempcounter2)+'\n'
            node.code+="sw $a0 "+str(1 * (activationStack.peek().get() - activationStack.peek().get(node.expr.name.name)))+'($fp)\n'
        else :
            self.visit(node.expr)
            if node.expr is not None:
                node.code+=node.expr.code
                node.code+='beq $a0 0 l'+str(tempcounter2)+'\n'
        self.visit(node.truebranch)
        node.code+=node.truebranch.code
        node.code+='j l'+str(tempcounter)+'\n'
        node.code+='l'+str(tempcounter2)+':\n'
        if isinstance(node.expr,Forloop):
            node.code+='addiu $sp $sp 4\naddiu $sp $sp 4\n'
            node.code+='lw $t4 8($sp)\nlw $t5 4($sp)\nsw $t4 4($sp)\nsw $t5 8($sp)\naddiu $fp $fp 4\naddiu $sp $sp 4\n'
            activationStack.peek().remove()
        node.code+='ll'+str(tempwhileCounter)+':\n'
        whilePointer-=1

    def visit_Doubledotrange(self,node):
        self.visit(node.left)
        node.code=node.left.code
        node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'
        self.visit(node.right)
        node.code+=node.right.code
        node.code+='sw $a0 0($sp)\naddiu $sp $sp -4\n'

    def visit(self, node):
        if node is not None:
            function_name = 'visit_' + node.__class__.__name__
            function = getattr(self, function_name)
            function(node)


class JumpGenerator(block.BlockVisitor):
    def visit_BasicBlock(self,block):
        print("Block:[%s]" % block)
        for inst in block.instructions:
            print("    %s" % (inst,))
        print("")

    def visit_IfBlock(self,block):
        self.visit_BasicBlock(block)
        if block.falsebranch:
            pass
        self.visit(block.truebranch)
        if block.falsebranch:
            self.visit(block.falsebranch)


    def visit_WhileBlock(self,block):
        self.visit_BasicBlock(block)
        self.visit(block.truebranch)



def generate_code(tree):
    gen = GenerateCode()
    gen.visit(tree)
    return gen.code


def initialize_types(typechecker):
    global IntType
    IntType = typechecker.Int
    global FloatType
    FloatType = typechecker.Float
    global StringType
    StringType = typechecker.Str
    global BoolType
    BoolType = typechecker.Bool
    #Enum = Enumeration()
    global CharType
    CharType = typechecker.Char
    global ArrayType
    ArrayType = typechecker.Arr


def tracefunc(frame, event, arg, indent=[0]):
      if event == "call":
          indent[0] += 2
          print "-" * indent[0] + "> call function", frame.f_code.co_name
      elif event == "return":
          print "<" + "-" * indent[0], "exit function", frame.f_code.co_name
          indent[0] -= 2
      return tracefunc

import sys
#sys.settrace(tracefunc)


def main():
    lexer = adalex.make_lexer()
    tokens = adalex.tokens
    parser = adaparse.make_parser()
    fpath = sys.argv[1] #input file path
    global filepath
    filepath = fpath
    program = parser.parse(open(fpath).read())
    cwd = os.getcwd() #gettign the current working directory
    slash, dot = fpath.rfind('/'), fpath.rfind('.')
    gfilename = fpath[slash+1:dot] # getting the input canonical file name stripping of the rest

    # Check the program
    typechecker = typecheck.typecheck()
    initialize_types(typechecker)
    env = typechecker.check_goal_symbol(program)

    if typechecker.get_error_count() > 0:
        print "Fix the type errors and compile again"
        sys.exit(0)
    # If no errors occurred, generate code
    code = generate_code(program)
    gen_file = cwd + "/assembly/" + gfilename + ".asm" #forming the output file name
    try:
        fd = open(gen_file, "w")
        fd.write(code)
        fd.flush()
        fd.close()
    except IOError:
        print "folder cannot be created"
    print "Done"
    # Emit the code sequence
    JumpGenerator().visit(code)


if __name__ == '__main__':
    main()


