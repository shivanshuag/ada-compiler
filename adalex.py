# ------------------------------------------------------------
# tokrules.py
#
# Token rules for ada programming language
# 
# ------------------------------------------------------------
import sys
import ply.lex as lex
from ply.lex import TOKEN

digit = r'([0-9])'
hex_digit = r'([0-9A-F])'
letter = r'([A-Za-z])'
nondigit = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'
numeral = r'(' + digit + r'(_?' + digit + r')*)'
hex_numeral = r'(' + hex_digit + r'(_?' + hex_digit + r')*)'       
exponent = r'([eE](\+|-)?' + numeral + r')'
decimal = r'(' + numeral + r'(\.(' + numeral + r'))?)'
base_number = r'(' + numeral + r'\#(' + hex_numeral + r')(\.(' + hex_numeral + r'))?)'
number = r'(' + decimal + r'|' + base_number + r'|' + exponent + r')'
character = r'\'.\''
string = r'\"((\"\")|[^\"])*\"'
comment = r'--[^\n]*'
#comment = r'--[^\n]*'
tokens = (
  #reserved words
  'ABORT',
  'ABS',
  'ABSTRACT',
  'ACCEPT',
  'ACCESS',
  'ALIASED',
  'ALL',
  'AND',
  'ARRAY',
  'AT',
  'BEGIN',
  'BODY',
  'CASE',
  'CONSTANT',
  'DECLARE',
  'DELAY',
  'DELTA',
  'DIGITS',
  'DO',
  'ELSE',
  'ELSIF',
  'END',
  'ENTRY',
  'EXCEPTION',
  'EXIT',
  'FOR',
  'FUNCTION',
  'GENERIC',
  'GOTO',
  'IF',
  'IN',
  'IS',
  'LIMITED',
  'LOOP',
  'MOD',
  'NEW',
  'NOT',
  'NULL',
  'OF',
  'OR',
  'OTHERS',
  'OUT',
  'PACKAGE',
  'PRAGMA',
  'PRIVATE',
  'PROCEDURE',
  'PROTECTED',
  'RAISE',
  'RANGE',
  'RECORD',
  'REM',
  'RENAMES',
  'REQUEUE',
  'RETURN',
  'REVERSE',
  'SELECT',
  'SEPARATE',
  'SUBTYPE',
  'TAGGED',
  'TASK',
  'TERMINATE',
  'THEN',
  'TYPE',
  'UNTIL',
  'USE',
  'WHEN',
  'WHILE',
  'WITH',
  'XOR',
  #operarors
  'DIV',
  'MUL',
  'ADD',
  'SUB',
  'ASSIGNMENT',
  'NOT_EQ',
  'GRE_EQ',
  'LESS_EQ',
  'LESS_LESS',
  'GRE_GRE',
  'BOX',
  'LESS',
  'GRE',
  'RIGHT_SHAFT',
  'EQ',
  'BAR',
  'AMPERSAND',
  'EXPONENT',
  'APOST',
  'COMMA',
  'DOT',
  'COLON',
  'SEMI_COLON',
  'DOT_DOT',
  'COMMENT',
  'IDENTIFIER',
  'NUMBER',
  'STRING',
  'CHARACTER',
  'NEWLINE',
  'TAB',
  'BRA_OPEN',
  'BRA_CLOSE',
  'TICK',

)

reserved = {
  'ABORT':'ABORT',
  'ABS':'ABS',
  'ABSTRACT':'ABSTRACT',
  'ACCEPT':'ACCEPT',
  'ACCESS':'ACCESS',
  'ALIASED':'ALIASED',
  'ALL':'ALL',
  'AND':'AND',
  'ARRAY':'ARRAY',
  'AT':'AT',
  'BEGIN':'BEGIN',
  'BODY':'BODY',
  'CASE':'CASE',
  'CONSTANT':'CONSTANT',
  'DECLARE':'DECLARE',
  'DELAY':'DELAY',
  'DELTA':'DELTA',
  'DIGITS':'DIGITS',
  'DO':'DO',
  'ELSE':'ELSE',
  'ELSIF':'ELSIF',
  'END':'END',
  'ENTRY':'ENTRY',
  'EXCEPTION':'EXCEPTION',
  'EXIT':'EXIT',
  'FOR':'FOR',
  'FUNCTION':'FUNCTION',
  'GENERIC':'GENERIC',
  'GOTO':'GOTO',
  'IF':'IF',
  'IN':'IN',
  'IS':'IS',
  'LIMITED':'LIMITED',
  'LOOP':'LOOP',
  'MOD':'MOD',
  'NEW':'NEW',
  'NOT':'NOT',
  'NULL':'NULL',
  'OF':'OF',
  'OR':'OR',
  'OTHERS':'OTHERS',
  'OUT':'OUT',
  'PACKAGE':'PACKAGE',
  'PRAGMA':'PRAGMA',
  'PRIVATE':'PRIVATE',
  'PROCEDURE':'PROCEDURE',
  'PROTECTED':'PROTECTED',
  'RAISE':'RAISE',
  'RANGE':'RANGE',
  'RECORD':'RECORD',
  'REM':'REM',
  'RENAMES':'RENAMES',
  'REQUEUE':'REQUEUE',
  'RETURN':'RETURN',
  'REVERSE':'REVERSE',
  'SELECT':'SELECT',
  'SEPARATE':'SEPARATE',
  'SUBTYPE':'SUBTYPE',
  'TAGGED':'TAGGED',
  'TASK':'TASK',
  'TERMINATE':'TERMINATE',
  'THEN':'THEN',
  'TYPE':'TYPE',
  'UNTIL':'UNTIL',
  'USE':'USE',
  'WHEN':'WHEN',
  'WHILE':'WHILE',
  'WITH':'WITH',
  'XOR':'XOR'
}
t_DIV = r'\/'
t_MUL = r'\*'
t_ADD = r'\+'
t_SUB = r'-'
t_ASSIGNMENT = r':='
t_NOT_EQ = r'\/='
t_GRE_EQ = r'>='
t_LESS_EQ = r'<='
#t_GRE_EQ = r'>='
t_LESS_LESS = r'<<'
t_GRE_GRE = r'>>'
t_BOX = r'<>'
t_LESS = r'<'
t_GRE = r'>'
t_RIGHT_SHAFT = r'=>'
t_EQ = r'='
t_BAR = r'\|'
t_AMPERSAND = r'&'
t_EXPONENT = r'\*\*'
t_APOST = r'\''
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_SEMI_COLON = r';'
t_DOT_DOT = '\.\.'
t_TICK = r'\''
#t_IDENTIFIER  
#t_NUMBER
#t_STRING
#t_CHARACTER
#t_NEWLINE
t_TAB = r'\t'
t_BRA_OPEN = r'\('
t_BRA_CLOSE = r'\)'

# @TOKEN(decimal)
# def t_DECIMAL(t):
#   t.value = t.value.replace('_','')
#   if '.' in t.value:
#     t.value = float(t.value)
#   else:
#     t.value = int(t.value)
#   return t

# @TOKEN(base_number)
# def t_BASE_NUMBER(t):


# @TOKEN(number)
# def t_NUMBER(t):
#   t.value = t.value.upper()
#   return t

def __is_valid(x, base):
    a = "0123456789abcdef"
    c = a[0:base]
    p = r"[^" + c + "_.]+"
    if re.search(p, x, re.I) != None:
            return False
    return True

def t_NUMBER(t):
    r'(?:(?:[0-9](_?[0-9])*\#[0-9a-fA-F](_?[0-9a-fA-F])*(\.?[0-9a-fA-F](_?[0-9a-fA-F])*)?\#([Ee][+\-]?[0-9](_?[0-9])*)?)|[0-9](_?[0-9])*(?:(?:\.[0-9](_?[0-9])*([Ee][+\-]?[0-9](_?[0-9])*)?)|(?:([Ee][+\-]?[0-9](_?[0-9])*)?)))'
    t.value = t.value.replace('_','')
    if '#' in t.value:
        h1 = t.value.index('#')
        h2 = h1 + t.value[h1+1:].index('#') + 1
        base, num, exp = t.value[0:h1], t.value[h1+1:h2], t.value[h2+1:]
        ##print base, num, exp
        if exp !=None and len(exp) > 0:
            exp = exp[1:]
            exp = int(exp)
        else: exp = 0
        base = int(base)
        if base <= 1 or base > 16: print "WARNING: Invalid base of the number used"
        if __is_valid(num, base) == False:
            print "WARNING: Incorrect symbols used in the number with base",base
        if '.' not in num:
            #its a integer
            num = int(num, base)
            t.value = num*pow(base, exp)
    elif '.' in t.value or 'e' in t.value or 'E' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t



@TOKEN(identifier)
def t_IDENTIFIER(t):
  t.value = t.value.upper()
  t.type = reserved.get(t.value,'IDENTIFIER')
  return t

@TOKEN(character)
def t_CHARACTER(t):
  t.value = t.value.upper()
  return t

@TOKEN(string)
def t_STRING(t):
  t.value = t.value.upper()
  return t

@TOKEN(comment)
def t_COMMENT(t):
  pass

def t_NEWLINE(t):
  r'\n+'
  t.lexer.lineno += t.value.count("\n")

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_error(t):
  print("Illegal character %s" % repr(t.value[0]))
  print "on line no. "+str(t.lexer.lineno)
  t.lexer.skip(1)

def make_lexer():
  return lex.lex();

def main():
  fileName = sys.argv[1]
  f = open(fileName, 'r')
  lexer = make_lexer()
  lexer.input(f.read())
  while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok

if __name__ == "__main__":
    main()