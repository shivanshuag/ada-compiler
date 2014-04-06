# -----------------------------------------------------------------------------
# type.py
#
# Specifies different types in ada for type checking
# -----------------------------------------------------------------------------
class Nill():
	def __init__(self):
		self.name = "Nill"

class Integer():
	name="Integer"
	def __init__(self, value):
		self.value = value

class Array():
	name = "Array"
	def __init__(self, array_type, ranges):
		self.type = array_type
		self.ranges = ranges

class Character():
	name="Character"
	def __init__(self, value):
		self.value = value

class Float():
	name="Integer"
	def __init__(self, value):
		self.value = value

class String():
	name="String"
	def __init__(self, value):
		self.value = value

class Boolean():
	name = "Boolean"
	def __init__(self, value):
		self.value = value

# class enumeration():


class Type():
	def __init__(self, name,value):
		self.name = name
		self.value = value

# 	def __init__(self, name, type__range):
# 		self.name = name
# 		self.range = type__range

# class subtype():
# 	def __init(self, parentType, type__range):
# 		self.parentType = parentType
# 		self.range = type__range

class range():
	def __init__(self, start, end):
		self.start = start
		self.end = end

