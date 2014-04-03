# -----------------------------------------------------------------------------
# symbol.py
#
# Symbol table for ada-compiler
# -----------------------------------------------------------------------------

class symtable():
	parent = {}
	def __init__(self, parentDict):
		self.parent = parentDict
	symbols = {}
