# -----------------------------------------------------------------------------
# symbol.py
#
# Symbol table for ada-compiler
# -----------------------------------------------------------------------------

class symtable():
	
	def __init__(self, parentDict):
		self.parent = parentDict
		self.symbols = {}

	def lookup(self, name):
		table = self
		while table.parent != None:
			if name in table.symbols.keys():
				return table[name]
			table = table.parent
		return None	