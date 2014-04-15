# -----------------------------------------------------------------------------
# datatypes.py
#
# Different data types supported by the compiler
# -----------------------------------------------------------------------------
class Integer():
  name = 'Integer'
  binary = {"+", "-", "*", "/","mod","rem","**"}
  unary = {"+", "-","abs"}
  rel = {"=", "/=", "<", ">", "<=", ">=","in","notin"}
  binary_opcodes = {"+": "add", "-": "sub", "*": "mul", "/": "div","**": "pow","mod": "mod","rem":"rem"}
  unary_opcodes = {"+": "uadd", "-": "uneg","abs":"abs"}
  #binary_folds = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv, "**": operator.pow, "mod": operator.mod}
  #unary_folds = {"+": operator.pos, "-": operator.neg}
  rel_opcodes = {"=": "seq", "/=": "sne", ">": "sgt", "<": "slt", ">=": "sge", "<=": "sle","in":"in","notin":"notin"}
  #rel_folds = {"=": operator.eq, "/=": operator.ne, ">": operator.gt, ">=": operator.ge,
  #           "<": operator.lt, "<=": operator.le}
  default = int() 

class Float():
  name = 'Float'
  binary = {"+", "-", "*", "/"}
  unary = {"+", "-","abs"}
  rel = {"=", "/=", "<", ">", "<=", ">="}
  binary_opcodes={"+": "add.s", "-": "sub.s", "*": "mul.s", "/": "div.s"}
  unary_opcodes={"+": "uadd", "-": "uneg","abs":"abs"}
  #binary_folds={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv},
  #unary_folds={"+": operator.pos, "-": operator.neg}
  rel_opcodes={"=": "seq.s", "/=": "sne.s", ">": "sgt.s", "<": "slt.s", ">=": "sge.s", "<=": "sle.s"}
  # rel_folds={"=": operator.eq, "/=": operator.ne, ">": operator.gt, ">=": operator.ge,
  #            "<": operator.lt, "<=": operator.le}
  default = float() 


class String():
  name = "String"
  binary = {"&"}
  binary_opcodes={"&":"ampersand"}
  #binary_folds={"&": operator.add}
  default = str() 


class Character():
  name="Character"
  default = chr(0)

class Boolean():
  name = "Boolean"
  unary={"!"},
  rel={"=", "/=", "and", "or","xor","andthen","orelse"},
  rel_opcodes={"=": "seq", "/=": "sne", "and": "land", "or": "lor", "xor": "lxor","andthen":"andthen","orelse":"orelse"}
  #rel_folds={"=": operator.eq, "/=": operator.ne, "&&": operator.and_, "||": operator.or_},
  unary_opcodes={"!": "not"},
  #unary_folds={"!": operator.not_}
  default = bool() 

class Array():
  name = "Array"
  default = list()

class Enumeration():
  name = "Enum"
  default = None