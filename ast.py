# -----------------------------------------------------------------------------
# ast.py
#
# Defines structure of ast for the compiler
# -----------------------------------------------------------------------------

class ast():
	def __init__(self,*args,**kwargs):
		field_tuples = zip(self.fields, args)
		#For each of the field in the respective subclass, we create object properties 
		for field,value in field_tuples:
			setattr(self, field, value)
		for name,value in kwargs.items():
            setattr(self,name,value)


#All the classes below inherit the ast class. Each class defines a list of fields for the ast node.
#ast class creates the properties for those fields in the object of the class
class goal_symbol(ast):
    fields = ['compilation']          

class compilation(ast):
    fields = ['comp_unit']
    def new_comp_unit(self,unit):
		self.comp_unit.append(unit)

    # def len(self):
    #     return len(self.program)

# class comp_unit(ast):
# 	fields = ['context_spec', 'unit']

# class context_spec(ast):
# 	fields = ['package_with', 'package_use']
# 	def new_context_spec(self, package_with, package_use):
# 		self.package_with.append(package_with)
# 		self.package_use.append(package_use)

# class package_with(ast):
# 	fields = ['name']

# class package_use(ast):
# 	fields = ['name']

class Literal(ast):
    fields = ['value']          

class Typename(ast):
    fields = ['name']          

class Location(ast):
    fields = ['name']          

class LoadLocation(ast):
    fields = ['location']          

class Unaryop(ast):
    fields = ['op','expr']           

class Binop(ast):
    fields = ['op','left','right']          
    
class Relop(ast):
    fields = ['op','left','right']          
    
class AssignmentStatement(ast):
    fields = ['location','expr']          

class ArrayAssignmentStatement(ast):
    fields = ['location','args','expr']          

class PrintStatement(ast):
    fields = ['expr']          
    
class Statements(ast):
    fields = ['statements']          

    def append(self,stmt):
        self.statements.append(stmt)

    def len(self):
        return len(self.statements)



class VariableDeclaration(ast):
    fields = ['name','typename','expr','length']          
  
class TypeDeclaration(ast):
	 fields = ['name', 'expr', 'typecompletion']   

class Integertype(ast):
    fields = ['rangespec', 'expression']

class Floattype(ast):
    fields = ['expression', 'rangespecopt']

class Fixedtype(ast):
    fields = ['expression1', 'rangespecopt', 'expression2']

class Accesstypesubtype(ast):
    fields = ['modifier', 'subtypeind']

class Accesstypesubprog(ast):
    fields = ['protopt', 'formalpartopt', 'mark']
     
class Unconstrarray(ast):
    fields = ['indexs','aliased','subtypeind']
    
class Constrarray(ast):
    fields = ['indexconstraint','aliased','subtypeind']

class Record(ast):
    fields = ['tagged',' limited','recorddef']

class Enum(ast):
    fields = ['enumid']
    
    def append(self,stmt):
        self.enumid.append(stmt)

    def len(self):
        return len(self.enumid) 

class ComponentDeclaration(ast):
    fields = ['compdecls']

    def append(self,compdecl):
        self.compdecls = self.compdecls + compdecl

    def len(self):
        return len(self.compdecls)

 
class Indexs(ast):
    fields = ['indexs']
    
    def append(self,stmt):
        self.indexs.append(stmt)

    def len(self):
        return len(self.indexs)

class IfStatement(ast):
    fields = ['expr', 'truebranch', 'falsebranch']

class CaseStatement(ast):
    fields = ['condition','alternatives']

class Alternatives(ast):
    fields = ['alternatives']

    def append(self,alternate):
        self.alternatives.append(alternate)

    def len(self):
        return len(self.alternatives)

class Alternative(ast):
    fields = ['choices','statements']

class Choices(ast):
    fields = ['choices']

    def append(self,choice):
        self.choices.append(choice)
    
    def len(self):
        return len(self.choices)

class WhileStatement(ast):
    fields = ['label','expr', 'truebranch','id']

class LoopStatement(ast):
    fields = ['condition','truebranch']

class Forloop(ast):
    fields = ['name','reverse','discreterange']

class Doubledotrange(ast):
    fields = ['left','right']

class Nametick(ast):
    fields = ['name','expression']

class Block(ast):
    fields = ['label','decl','block','id']

class FuncStatement(ast):
    fields = ['name', 'returntype', 'parameters','declpart','statements','id']

class FuncParameterList(ast):
    fields = ['parameters']

    def new_parameter(self,stmt):
        self.parameters = self.parameters + stmt

    def len(self):
        return len(self.parameters)

#below three classes were added by mohit

class FuncParameter(VarDeclaration):
    pass

class TypeDeclaration(VarDeclaration):
    pass

class SubTypeDeclaration(VarDeclaration):
    pass

class FuncCall(ast):
    fields = ['name','arguments']

class ProcCall(ast):
    fields = ['name']

class Values(ast):
    fields = ['arguments']

    def append(self,stmt):
        self.arguments.append(stmt)

    def len(self):
        return len(self.arguments)

class ReturnStatement(ast):
    fields = ['expr']

class ExitStatement(ast):
    fields = ['name','expr']

class GotoStatement(ast):
    fields = ['name']


