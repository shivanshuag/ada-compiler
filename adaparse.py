# -----------------------------------------------------------------------------
# adaparse.py
#
# Simple parser for ADA 95.  Based on the grammar from ADA Reference Manual
# -----------------------------------------------------------------------------

import sys
import adalex
import ply.yacc as yacc

from symbol import symtable
from type import *
# Get the token map
tokens = adalex.tokens
#table_prev = NULL
table_current = symtable(None)

types_declared = []
subtypes_declared = []

def p_goal_symmbol(t):
  'goal_symbol : compilation'
  print 'parsing complete'
#  print 'lineno.' + str(t.lexer.lineno)
  pass

def p_compilation(t):
  '''compilation :
                | compilation comp_unit
                '''
  pass

def p_comp_unit(t):
  '''comp_unit : context_spec private_opt unit
                | private_opt unit
                '''
def p_private_opt(t):
  '''private_opt :
                  | PRIVATE
                  '''
  pass

def p_context_spec(t):
  '''context_spec : with_clause use_clause_opt
                  | context_spec with_clause use_clause_opt
                  '''
  pass

def p_with_caluse(t):
  'with_clause : WITH c_name_list SEMI_COLON'
  pass

def p_c_name_list(t):
  '''c_name_list : compound_name
                  | c_name_list COMMA compound_name
                  '''
  pass

def p_use_clause_opt(t):
  '''use_clause_opt :
                    | use_clause_opt use_clause
                    '''
  pass

def p_unit(t):
  'unit : subprog_body'
  pass



def p_statement_s(t):
  '''statement_s : statement
                 | statement_s statement
                 '''
  pass

def p_statement(t):
  '''statement : unlabeled
               | label statement
               '''
  pass

def p_label(t):
  'label : LESS_LESS IDENTIFIER GRE_GRE'
  pass

def p_label_opt(t):
  '''label_opt :
               | label
               '''
  pass

def p_unlabeled(t):
  '''unlabeled : simple_stmt
               | compound_stmt
               '''
  pass

def p_simple_stmt(t):

#NOT Implemented - requeue_stmt
  '''simple_stmt : null_stmt
                 | assign_stmt
                 | exit_stmt
                 | return_stmt
                 | goto_stmt
                 | procedure_call
                 | delay_stmt
                 | abort_stmt
                 | raise_stmt
                 | code_stmt
                 | error SEMI_COLON
                 '''
  pass

def p_compound_stmt(t):
  #not implemented accept_stmt and select_stmt
  '''compound_stmt : if_stmt
                   | case_stmt
                   | loop_stmt
                   | block
                   '''
  pass



#grammar for simple_stmts
def p_null_stmt(t):
  'null_stmt : NULL SEMI_COLON'
  pass

def p_assign_stmt(t):
  'assign_stmt : name ASSIGNMENT expression SEMI_COLON'
  pass

def p_exit_stmt(t):
  'exit_stmt : EXIT name_opt when_opt SEMI_COLON'
  pass

def p_return_stmt(t):
  '''return_stmt : RETURN SEMI_COLON
                 | RETURN expression SEMI_COLON
                 '''
  pass

def p_goto_stmt(t):
  'goto_stmt : GOTO name SEMI_COLON'
  pass

def p_procedure_call(t):
  'procedure_call : name SEMI_COLON'
  pass

def p_delay_stmt(t):
  '''delay_stmt : DELAY expression SEMI_COLON
                | DELAY UNTIL expression SEMI_COLON
                '''
  pass

def p_abort_stmt(t):
  'abort_stmt : ABORT name_s SEMI_COLON'

def p_raise_stmt(t):
  'raise_stmt : RAISE name_opt SEMI_COLON'
  pass

def p_code_stmt(t):
  'code_stmt : qualified SEMI_COLON'
  pass




#grammar for if statements
def p_if_stmt(t):
  'if_stmt : IF cond_clause_s else_opt END IF SEMI_COLON'
  pass

def p_cond_clause_s(t):
  '''cond_clause_s : cond_clause
                   | cond_clause_s ELSIF cond_clause
                   '''
  pass

def p_cond_clause(t):
  'cond_clause : cond_part statement_s'
  pass

def p_cond_part(t):
  'cond_part : condition THEN'
  pass

def p_condition(t):
  'condition : expression'
  pass

def p_else_opt(t):
  '''else_opt :
              | ELSE statement_s
              '''
  pass



#grammar for case_stmt
def p_case_stmt(t):
  'case_stmt : case_hdr alternative_s END CASE SEMI_COLON'
  pass

def p_case_hdr(t):
  'case_hdr : CASE expression IS'
  pass

def p_alternative_s(t):
  '''alternative_s :
                   | alternative_s alternative'''
  pass

def p_alternative(t):
  'alternative : WHEN choice_s RIGHT_SHAFT statement_s'
  pass



#grammar for loop stmt
def p_loop_stmt(t):
  'loop_stmt : iteration basic_loop id_opt SEMI_COLON'
  pass

def p_iteration(t):
  '''iteration :
                | WHILE condition
                | iter_part reverse_opt discrete_range
                '''
  pass

def p_iter_part(t):
  'iter_part : FOR IDENTIFIER IN'
  pass

def p_reverse_opt(t):
  '''reverse_opt :
                 | REVERSE'''
  pass

def p_basic_loop(t):
  'basic_loop : LOOP statement_s END LOOP'
  pass

def p_id_opt1(t):
  'id_opt :'
  t[0] = ['NilExp', t.lexer.lineno]
  pass

def p_id_opt2(t):
  'id_opt : designator'
  t[0] = t[1]
  pass

def p_designator1(t):
  'designator : compound_name'
  t[0] = t[1]

def p_designator2(t):
  'designator : STRING'
  t[0] = ['StringExp', t.lexer.lineno, table_current,t[1]]
  pass


#grammar for block
def p_block(t):
  'block : label_opt block_decl block_body END id_opt SEMI_COLON'
  pass

def p_block_body(t):
  #not implemented handled_statement_s
  'block_body : BEGIN statement_s'
  pass

def p_block_decl(t):
  '''block_decl :
                | DECLARE decl_part
                '''
  pass

def p_decl_part(t):
  '''decl_part :
               | decl_item_or_body_s1'''
  pass

def p_decl_item_or_body_s1(t):
  '''decl_item_or_body_s1 : decl_item_or_body
                  | decl_item_or_body_s1 decl_item_or_body
                  '''
  pass

def p_decl_item_or_body(t):
  '''decl_item_or_body : body
                        | decl_item
                        '''
  pass

def p_decl_item(t):
  #rep_spec not implemented
  'decl_item : decl'

def p_decl_item1(t):
  'decl_item : use_clause'
  print 'error: not implemented use clause in declaration in line number'+ t.lexer.lineno
  pass

#grammar for use_clause
def p_use_clause(t):
  '''use_clause : USE name_s SEMI_COLON
                | USE TYPE name_s SEMI_COLON
                '''
  pass



#grammar for decl
def p_decl(t):
  #not implemented - pkg_decl, task_decl, prot_decl, exception_decl, rename_decl, generic_decl, body_stub
  '''decl : object_decl
          | number_decl
          | type_decl
          | subtype_decl
          | subprog_decl
          | error SEMI_COLON
          '''
  pass

#grammar for object decl
def p_object_decl(t):
  'object_decl : def_id_s COLON object_qualifier_opt object_subtype_def init_opt SEMI_COLON'
#pushing in symbol table
  if DEBUG :
    print table_current.symbols.keys() 
  for i in t[1]:
    if i[1] not in table_current.symbols.keys():
        if DEBUG :
          print 'adding symbol '+ i[1]
        if t[4][0] == 'StringExp':
          if t[4][4] == 'INTEGER':
            table_current.symbols[i[1]] = ['ObjectTy', Integer(None), t.lexer.lineno, t[3], t[4], t[5]]
          elif t[4][4] == 'CHARACTER':
            table_current.symbols[i[1]] = ['ObjectTy', Character(None), t.lexer.lineno, t[3], t[4], t[5]]
          elif t[4][4] == 'BOOLEAN':
            table_current.symbols[i[1]] = ['ObjectTy', Boolean(None), t.lexer.lineno, t[3], t[4], t[5]]
          elif t[4][4] == 'FLOAT':
            table_current.symbols[i[1]] = ['ObjectTy', Float(None), t.lexer.lineno, t[3], t[4], t[5]]
        elif t[4][0] == 'ConarraydefExp' :
          #TODO array constraint can be a name of a type
          #TODO make ranges of the class declared in type.py. Currently range is given as ast of the subtree
          table_current.symbols[i[1]] = ['ObjectTy', Array(t[4][4][4], t[4][3]), t.lexer.lineno, t[3], t[4], t[5]]
    else:
      print 'error : redeclaration of variable ' + i[1] + ' on line number ' + str(i[0])

def p_def_id_s1(t):
  'def_id_s : def_id'
  t[0] = [(t.lexer.lineno, t[1])]
  # global table_current
  # if t[1] not in table_current.keys():
  #   table_current[t[1]] = {'init': 0}

def p_def_id_s2(t):
  'def_id_s : def_id_s COMMA def_id'
  t[0] = t[1].insert((t.lexer.lineno, t[3]))
  # global table_current
  # if t[1] not in table_current.keys():
  #   table_current[t[1]] = {'init': 0}

def p_def_id(t):
  'def_id  : IDENTIFIER'
  t[0] = t[1]
  pass

def p_object_qualifier_opt(t):
  'object_qualifier_opt : '
  t[0] = ""

def p_object_qualifier_opt1(t):
  ''' object_qualifier_opt : ALIASED
                          | CONSTANT
                          | ALIASED CONSTANT
                          '''
  t[0] = t[1]
  pass

def p_object_subtype_def(t):
  '''object_subtype_def : subtype_ind
                        | array_type
                        '''
  t[0] = t[1]
  pass

def p_init_opt1(t):
  'init_opt : '
  t[0] = ['NilExp', t.lexer.lineno]
  pass

def p_init_opt2(t):
  'init_opt : ASSIGNMENT expression'
  t[0] = t[2]
  pass

#grammar for number_decl
def p_number_decl(t):
  'number_decl : def_id_s COLON CONSTANT ASSIGNMENT expression SEMI_COLON'
  for i in t[1]:
    if i not in table_current.symbols.keys():
        table_current.symbols[i[1]] = ['NumTy', t.lexer.lineno, t[5]]
    else:
      print 'error : redeclaration of variable ' + i[1] + ' on line number ' + i[0]

  pass

#grammar for type_decl
def p_type_decl(t):
  #discrim_part not implemented
  'type_decl : TYPE IDENTIFIER type_completion SEMI_COLON'
  pass

def p_type_completion(t):
  '''type_completion :
                      | IS type_def
                      '''
  pass

def p_type_def(t):
  # not implemented record_type, access_type, derived_type, private_type
  '''type_def : enumeration_type 
              | integer_type
              | real_type
              | array_type
              '''
  t[0] = t[1]
  pass

def p_enumeration_type(t):
  'enumeration_type : BRA_OPEN enum_id_s BRA_CLOSE'
  t[0] = ['EnumExp', t[2]]
  pass

def p_enum_id_s(t):
  '''enum_id_s : enum_id
              | enum_id_s COMMA enum_id
              '''
  pass

def p_enum_id(t):
  '''enum_id : IDENTIFIER
            | CHARACTER
            '''
  pass

def p_integer_type(t):
  '''integer_type : range_spec
                  | MOD expression
                  '''
  pass
  
def p_range_spec_opt(t):
  '''range_spec_opt :
                    | range_spec
                    '''
  pass

def p_range_spec(t):
  'range_spec : range_constraint'
  pass

def p_range_constraint(t):
  'range_constraint : RANGE range'
  t[0] = t[2]
  pass
def p_range1(t):
  'range : simple_expression DOT_DOT simple_expression'
  t[0] = ['OpExp', t.lexer.lineno, t[1], t[2], t[3]]

def p_range2(t):
  '''range : name TICK RANGE
           | name TICK RANGE BRA_OPEN expression BRA_CLOSE
           '''
  t[0] = t[1]
  pass

def p_real_type(t):
  '''real_type : float_type
                | fixed_type
                '''
  pass

def p_float_type(t):
  'float_type : DIGITS expression range_spec_opt'
  pass

def p_fixed_type(t):
  '''fixed_type : DELTA expression range_spec
                | DELTA expression DIGITS expression range_spec_opt
                '''
  pass

def p_array_type(t):
  '''array_type : unconstr_array_type
                | constr_array_type
                '''
  t[0] = t[1]
  pass

def p_unconstr_array_type(t):
  'unconstr_array_type : ARRAY BRA_OPEN index_s BRA_CLOSE OF component_subtype_def'
  t[0] = ['UnconarraydefExp', t.lexer.lineno, t[3], t[6]]
  pass

def p_index_s(t):
  'index_s : index'
  t[0] = ['ExpList', t.lexer.lineno, t[1], None]
  pass
def p_index_s1(t):
  'index_s : index_s COMMA index'
  t[0] = ['ExpList', t.lexer.lineno, t[3], t[1]]
  pass

def p_index(t):
  'index : name RANGE BOX'
  t[0] = t[1]
  pass

def p_component_subtype_def(t):
  'component_subtype_def : aliased_opt subtype_ind'
  t[0] = t[2]
  pass

def p_aliased_opt(t):
  'aliased_opt : '
  t[0] = ['NilExp', t.lexer.lineno]
  pass

def p_aliased_opt1(t):
  'aliased_opt : ALIASED'
  t[0] = t[1]
  pass


def p_constr_array_type(t):
  'constr_array_type : ARRAY iter_index_constraint OF component_subtype_def'
  t[0] = ['ConarraydefExp', Nill(), t.lexer.lineno, t[2], t[4]]

  pass

def p_iter_index_constraint(t):
  'iter_index_constraint : BRA_OPEN iter_discrete_range_s BRA_CLOSE'
  t[0] = t[2]
  pass

def p_iter_discrete_range_s1(t):
  'iter_discrete_range_s : discrete_range'
  t[0] = ['ExpList', t.lexer.lineno, t[1]]
  pass
def p_iter_discrete_range_s2(t):
  'iter_discrete_range_s : iter_discrete_range_s COMMA discrete_range'
  t[0] = ['ExpList', t.lexer.lineno, t[3], t[1]]
  pass

def p_discrete_range(t):
  '''discrete_range : name range_constr_opt
                    | range
                    '''
  t[0] = t[1]
  pass

#grammar for subtype_decl
def p_subtype_decl(t):
  'subtype_decl : SUBTYPE IDENTIFIER IS subtype_ind SEMI_COLON'

  pass
  t[0] = ['NameConstr', t.lexer.lineno, t[1], t[2]]

def p_subtype_ind(t):
  'subtype_ind : name constraint'
  print "Not implemented constraint in declaration"
  t[0] = ['NameConstr', t.lexer.lineno, t[1], t[2]]
  pass

def p_subtype_ind1(t):
  'subtype_ind : name'
  t[0] = t[1]
  pass

def p_constraint(t):
  '''constraint : range_constraint
                | decimal_digits_constraint
                '''
  t[0] = t[1]
  pass

def p_decimal_digits_constraint(t):
  'decimal_digits_constraint : DIGITS expression range_constr_opt'
  t[0] = ['DecimalConstr', t.lexer.lineno, t[2], t[3]]
  pass

def p_range_constr_opt(t):
  'range_constr_opt : '
  t[0] = ['NilExp', t.lexer.lineno]
  pass
def p_range_constr_opt1(t):
  'range_constr_opt : range_constraint'
  t[0] = t[1]
  pass


#grammar for subprog_decl
def p_subprog_decl(t):
  # not implemented generic_subp_inst, and subprog_spec IS ABSTRACT SEMI_COLON

  '''subprog_decl : subprog_spec SEMI_COLON
                  '''
  pass

def p_subprog_spec1(t):
  'subprog_spec : PROCEDURE compound_name formal_part_opt'
  if DEBUG : 
    print 'started procedure ' + t[2][3]
  global table_current
  table = symtable(table_current)
  table_current.symbols[t[2][3]] = table
  table_current = table
  pass

def p_subprog_spec2(t):
  'subprog_spec : FUNCTION designator formal_part_opt RETURN name'
  if DEBUG : 
    print 'started function ' + t[2][3]
  global table_current
  table = symtable(table_current)
  table_current.symbols[t[2][3]] = table
  table_current = table
  pass

def p_subprog_spec3(t):
  'subprog_spec : FUNCTION designator'
  if DEBUG : 
    print 'started function ' + t[2][3]
  global table_current
  table = symtable(table_current)
  table_current.symbols[t[2][3]] = table  #TODO some problem here
  table_current = table
  pass

def p_formal_part_opt(t):
  '''formal_part_opt : 
                      | formal_part
                      '''
  pass

def p_formal_part(t):
  'formal_part : BRA_OPEN param_s BRA_CLOSE'
  pass

def p_param_s(t):
  '''param_s : param
              | param_s SEMI_COLON param
              '''
  pass

def p_param(t):
  '''param : def_id_s COLON mode mark init_opt
            | error
            '''
  pass

def p_mode(t):
  '''mode :
          | IN
          | OUT
          | IN OUT
          | ACCESS
          '''
  pass

# def p_discrim_part_opt(t):
#   '''discrim_part_opt :
#                       | discrim_part
#                       | BRA_OPEN BOX BRA_CLOSE
#                       '''
#   pass

# def p_discrim_part(t):
#   'discrim_part : BRA_OPEN discrim_spec_s BRA_CLOSE'
#   pass

# def p_discrim_spec_s(t):
#   '''discrim_spec_s : discrim_spec
#                     | discrim_spec_s SEMI_COLON discrim_spec
#                     '''
#   pass

# def p_discrim_spec(t):
#   '''discrim_spec : def_id_s COLON access_opt mark init_opt
#                   | error
#                   '''
#   pass

# def p_access_opt(t):
#   '''access_opt :
#                 | ACCESS
#                 '''
#   pass

def p_mark(t):
  '''mark : simple_name
          | mark TICK attribute_id
          | mark DOT simple_name
          '''
  pass

def p_attribute_id(t):
  '''attribute_id : IDENTIFIER
                  | DIGITS
                  | DELTA
                  | ACCESS
                  '''

#grammar for body
def p_body(t):
  'body : subprog_body'
  pass

def p_subprog_body(t):
  'subprog_body : subprog_spec IS decl_part block_body end_subprog'
  #table_current = symtable(NULL)
  pass

def p_end_subprog(t):
  'end_subprog : END id_opt SEMI_COLON'
  if DEBUG :
    print 'ended subprogram '+t[2][3]
  global table_current
  table_current = table_current.parent

  pass
#grammar for name
def p_name_s(t):
  '''name_s : name
            | name_s COMMA name
            '''
  pass

def p_name(t):
  #attribute not implemented
  '''name : simple_name
          | indexed_comp
          | selected_comp
          | attribute
          | operator_symbol
          '''
  t[0] = t[1]
  pass

def p_attribute(t):
  'attribute : name TICK attribute_id'
  pass

def p_name_opt(t):
  '''name_opt :
              | name
              '''
  pass

def p_simple_name(t):
  'simple_name : IDENTIFIER'
  #TODO find where use before declaration error is to be given
  t[0] = ['StringExp', Nill(), t.lexer.lineno, table_current, t[1]]
  pass

def p_indexed_comp(t):
  'indexed_comp : name BRA_OPEN value_s BRA_CLOSE'
  #TODO add suitable type information here
  t[0] = ['FuntionUse', Nill(), t.lexer.lineno, t[1],t[3]]
  pass


def p_selected_comp1(t):
  '''selected_comp : name DOT simple_name
                  | name DOT used_char
                  | name DOT operator_symbol
                  '''
  t[0] = ['OpExp', Nill() ,t.lexer.lineno, t[1],t[2],t[3]]

def p_selected_comp2(t):
  'selected_comp : name DOT ALL'
  t[0] = ['OpExp', Nill(), t.lexer.lineno, t[1], t[2], ['StringExp', t.lexer.lineno, table_current, "ALL"]]
  pass

def p_used_char(t):
  'used_char : CHARACTER'
  t[0] = ['StringExp', Character(t[1]), t.lexer.lineno, table_current, t[1]]
  pass

def p_operator_symbol(t):
  'operator_symbol : STRING'
  t[0] = ['StringExp', String(t[1]), t.lexer.lineno, table_current,t[1]]
  pass

def p_compound_name1(t):
  'compound_name : simple_name'
  t[0] = t[1]
  pass

def p_compound_name2(t):
  'compound_name : compound_name DOT simple_name'
  t[0]= ['OpExp',t.lexer.lineno, t[1], t[2], t[3]]
  pass

#
def p_when_opt(t):
  '''when_opt :
              | WHEN condition
              '''
  pass

#grammar for value
def p_value_s1(t):
  'value_s : value'
  t[0] = ['ExpList', t[1]]
  pass

def p_value_s2(t):
  'value_s : value_s COMMA value'
  t[0] = t[1].append(t[3])
  pass

def p_value(t):
  '''value : expression
           | comp_assoc
           | discrete_with_range
           '''
  t[0] = t[1]

def p_value1(t):
  'value : error'
  print 'error in lineno' + str(t.lexer.lineno)

def p_comp_assoc(t):
  'comp_assoc : choice_s RIGHT_SHAFT expression'
  pass

def p_choice_s(t):
  '''choice_s : choice
              | choice_s BAR choice
              '''
  pass

def p_choice(t):
  '''choice : expression
            | discrete_with_range
            | OTHERS
            '''
  pass

def p_discrete_with_range1(t):
  'discrete_with_range : name range_constraint'
  t[0] = t[1]
def p_discrete_with_range2(t):
  'discrete_with_range : range'
  t[0] = t[1]
  pass


# def p_qualified(t):
#   'qualified : '
#   pass

# def p_simple_expression(t):
#   'simple_expression :'
#   pass

#grammar for expression
def p_expression1(t):
  'expression : relation'
  t[0] = t[1]
  pass

def p_expression2(t):
  '''expression : expression logical relation
                | expression short_circuit relation
                '''
  if(t[1][1].name != "Boolean"):
    print 'error on line number '+str(t.lexer.lineno)+': type should be boolean'
  if(t[3][1].name != "Boolean"):
    print 'error on line number '+str(t.lexer.lineno)+': type should be boolean'
  t[0] = ['OpExp', t[1][1], t.lexer.lineno, t[1], t[2], t[3]]

def p_relation1(t):
  'relation : simple_expression'
  t[0] = t[1]

def p_relation2(t):
  '''realtion : simple_expression relational simple_expression
              | simple_expression membership range
              '''
  if(t[1][1].name != t[3][1].name):
    print 'type error on line number '+str(t.lexer.lineno)+': incompatible types'
  t[0] = ['OpExp', Boolean(None), t.lexer.lineno, t[1], t[2], t[3]]

def p_relation3(t):
  'relation : simple_expression membership name'
  #TODO check name should be subtype and type checking
  t[0] = ['OpExp', Boolean(None), t.lexer.lineno, t[1], t[2], t[3]]


def p_simple_expression1(t):
  'simple_expression : unary term'
  t[0] = ['UnaryOpExp', t[2][1], t.lexer.lineno, t[1], t[2]]
  pass

def p_simple_expression2(t):
  'simple_expression : term'
  t[0] = t[1]
  pass

def p_simple_expression3(t):
  'simple_expression : simple_expression adding term'
  if(t[1][1].name != t[3][1].name):
    print "type error on line number "+str(t.lexer.lineno)+": incompatible types "+t[1][1].name+"and "+t[3][1].name
  if(t[1][1].name != "Integer" or t[1][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"
  if(t[3][1].name != "Integer" or t[3][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"

  t[0] = ['OpExp', t[1][1], t.lexer.lineno, t[1], t[2], t[3]]
  pass

def p_unary(t):
  '''unary : ADD
           | SUB
           '''
  t[0] = ['UnaryOp',t[1]]
  pass

def p_adding(t):
  '''adding : ADD
            | SUB
            | AMPERSAND
            '''
  t[0] = ['AddBinaryOp',t[1]]
  pass

def p_term1(t):
  'term : factor'
  t[0] = t[1]
  pass

def p_term2(t):
  'term : term multiplying factor'
  if(t[1][1].name != t[3][1].name):
    print "type error on line number "+str(t.lexer.lineno)+": incompatible types "+t[1][1].name+"and "+t[3][1].name
  if(t[1][1].name != "Integer" or t[1][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"
  if(t[3][1].name != "Integer" or t[3][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"

  t[0] = ['OpExp', t[1][1], t.lexer.lineno, t[1], t[2], t[3]]
  pass

def p_multiplying(t):
  '''multiplying : MUL
                 | DIV
                 | MOD
                 | REM
                 '''
  t[0] = ['MultBinaryOp', t[1]]
  pass

def p_factor1(t):
  'factor : primary'
  t[0] = t[1]
  pass
def p_factor2(t):
  '''factor : NOT primary
            | ABS primary
            '''
  if(t[2][1].name != "Boolean"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be Boolean"
  t[0] = ['UnaryOpExp', t[2][1], t.lexer.lineno, t[1], t[2]]

def p_factor3(t):
  'factor : primary EXPONENT primary'
  if(t[1][1].name != t[3][1].name):
    print "type error on line number "+str(t.lexer.lineno)+": incompatible types "+t[1][1].name+"and "+t[3][1].name
  if(t[1][1].name != "Integer" or t[1][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"
  if(t[3][1].name != "Integer" or t[3][1].name != "Float"):
    print "type error on line number "+str(t.lexer.lineno)+": type should be either Integer or Float"

  t[0] = ['OpExp', t[1][1], t.lexer.lineno, t[1], t[2], t[3]]
  pass

def p_primary1(t):
  #Allocator not implemented
  '''primary : literal
            | parenthesized_primary
            '''
  t[0] = t[1]

def p_primary2(t):
  #Allocator not implemented
  '''primary : name
             | allocator
             | qualified
             '''
  if t[1][0] == 'StringExp':
    identifier = table_current.lookup(t[1][4])
    if(identifier == None):
      print 'error on line number '+str(t.lexer.lineno)+': identifier '+t[1][4]+'used before declaration'
  t[0] = t[1]
  pass

def p_parenthesized_primary1(t):
  'parenthesized_primary : aggregate'
  t[0] = ['NotImplemented', t.lexer.lineno, 'Aggregate not implemented']
  print 'Not Implemented aggregate in line no' + str(t.lexer.lineno)

def p_parenthesized_primary2(t):
  'parenthesized_primary : BRA_OPEN expression BRA_CLOSE'
  t[0] = t[1]
  pass

def p_qualified (t):
  'qualified : name TICK parenthesized_primary'
  t[0] = ['OpExp', t.lexer.lineno, t[1], t[2], t[3]]
  pass

def p_allocator (t):
  '''allocator : NEW name 
               | NEW qualified
               '''
  pass

def p_literal1(t):
  'literal : NUMBER '
  if(t[1].find('.') == -1):
    t[0] = ['NumberExp', Integer(t[1]), t.lexer.lineno, t[1]]
  else:
    t[0] = ['NumberExp', Float(t[1]), t.lexer.lineno, t[1]]

def p_literal2(t):
  'literal : used_char'
  t[0] = t[1]

def p_literal3(t):
  'literal : NULL'
  t[0] = ['NullExp', Null(), t.lexer.lineno, t[1]] 
  pass

def p_aggregate(t):
  '''aggregate : BRA_OPEN comp_assoc BRA_CLOSE
               | BRA_OPEN value_s_2 BRA_CLOSE
               | BRA_OPEN expression WITH value_s BRA_CLOSE
               | BRA_OPEN expression WITH NULL RECORD
               | BRA_OPEN NULL RECORD BRA_CLOSE
               '''
  pass

def p_value_s_2(t):
  '''value_s_2 : value COMMA value
               | value_s_2 COMMA value
               '''
  pass

def p_relational(t):
  '''relational : EQ
                | NOT_EQ
                | LESS
                | GRE
                | LESS_EQ
                | GRE_EQ
                '''
  t[0] = t[1]
  pass

def p_membership1(t):
  'membership : IN'
  t[0] = t[1]

def p_membership2(t):
  'membership : NOT IN'
  t[0] = t[1]+' '+t[2]

def p_logical(t):
  '''logical : AND
             | OR
             | XOR
             '''
  t[0] = t[1]

def p_short_circuit(t):
  '''short_circuit : AND THEN
                   | OR ELSE
                   '''
  t[0] = t[1]
  pass

def p_error(t):
  '''error : '''
  print 'error on'+str(t)

parser = yacc.yacc()

fileName = sys.argv[1]
DEBUG = 0
if(len(sys.argv) > 2):
  DEBUG = 1
f = open(fileName, 'r')
result = parser.parse(f.read())
print result