class Block(object):
    def __init__(self):
        self.instructions = []   # Instructions in the block
        self.next = None   # Link to the next block

    def append(self,instr):
        self.instructions.append(instr)

    def __iter__(self):
        return iter(self.instructions)

class BasicBlock(Block):
    pass

class FuncBlock(Block):
    pass

class IfBlock(Block):
    def __init__(self):
        super(IfBlock, self).__init__()
        self.truebranch = None
        self.falsebranch = None

class WhileBlock(Block):
    def __init__(self):
        super(WhileBlock, self).__init__()
        self.truebranch = None

class BlockVisitor(object):
    def visit(self,block):
        while block:
            name = "visit_%s" % type(block).__name__
            if hasattr(self,name):
                getattr(self,name)(block)
            block = getattr(block, "next", None)


