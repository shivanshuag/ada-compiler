# -----------------------------------------------------------------------------
# symbol.py
#
# Symbol table for ada-compiler
# -----------------------------------------------------------------------------

class symtable():
	
	def __init__(self, parentDict, astnode):
		self.parent = parentDict
		self.symbols = {}
		self.astnode = astnode
	def lookup(self, name):
		table = self
		while table.parent != None:
			if name in table.symbols.keys():
				return table.symbols[name]
			table = table.parent
		return None	
	def return_type():
		if self.astnode:
			if self.astnode.returntype != None:
				return self.astnode.returntype.check_type
		return None
