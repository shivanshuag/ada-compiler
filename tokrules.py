# ------------------------------------------------------------
# tokrules.py
#
# Token rules for ada programming language
# 
# ------------------------------------------------------------



tokens = (
  #reserved words
  'ABORT',
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
  'WHEN'
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
  'GRE_EQ',
  'LESS_LESS',
  'GRE_GRE',
  'LESS_GRE',
  'LESS',
  'GRE',
  'DO_THIS',
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
  'ARRAY':'ARRAY'
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


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
