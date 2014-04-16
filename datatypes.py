# -----------------------------------------------------------------------------
# datatypes.py
#
# Different data types supported by the compiler
# -----------------------------------------------------------------------------
class Integer():
  name = 'Integer'
  binary = {"+", "-", "*", "/","MOD","REM","**"}
  unary = {"+", "-","ABS"}
  rel = {"=", "/=", "<", ">", "<=", ">=","IN","NOTIN"}
  binary_opcodes = {"+": "add", "-": "sub", "*": "mul", "/": "div","**": "pow","MOD": "mod","REM":"rem"}
  unary_opcodes = {"+": "uadd", "-": "uneg","ABS":"abs"}
  #binary_folds = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv, "**": operator.pow, "mod": operator.mod}
  #unary_folds = {"+": operator.pos, "-": operator.neg}
  rel_opcodes = {"=": "seq", "/=": "sne", ">": "sgt", "<": "slt", ">=": "sge", "<=": "sle","IN":"in","NOTIN":"notin"}
  #rel_folds = {"=": operator.eq, "/=": operator.ne, ">": operator.gt, ">=": operator.ge,
  #           "<": operator.lt, "<=": operator.le}
  default = int() 

class Float():
  name = 'Float'
  binary = {"+", "-", "*", "/"}
  unary = {"+", "-","ABS"}
  rel = {"=", "/=", "<", ">", "<=", ">="}
  binary_opcodes={"+": "add.s", "-": "sub.s", "*": "mul.s", "/": "div.s"}
  unary_opcodes={"+": "uadd", "-": "uneg","ABS":"abs"}
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
  rel={"=", "/=", "AND", "OR","XOR","ANDTHEN","ORELSE"},
  rel_opcodes={"=": "seq", "/=": "sne", "AND": "land", "OR": "lor", "XOR": "lxor","ANDTHEN":"andthen","ORELSE":"orelse"}
  #rel_folds={"=": operator.eq, "/=": operator.ne, "&&": operator.and_, "||": operator.or_},
  unary_opcodes={"!": "NOT"},
  #unary_folds={"!": operator.not_}
  default = bool() 

class Array():
  name = "Array"
  default = list()

class Enumeration():
  name = "Enum"
  default = None

class Undeclared():
  name = "Undeclared"
  default = None