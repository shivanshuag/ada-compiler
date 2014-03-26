# -----------------------------------------------------------------------------
# adaparse.py
#
# Simple parser for ADA 95.  Based on the grammar from ADA Reference Manual
# -----------------------------------------------------------------------------

import sys
import adalex
import ply.yacc as yacc

# Get the token map
tokens = adalex.tokens

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

#TODO: add LT_LT and GT_GT
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
  'loop_stmt : label_opt iteration basic_loop id_opt SEMI_COLON'
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

def p_id_opt(t):
  '''id_opt :
            | designator
            '''
  pass

def p_designator(t):
  '''designator : compound_name
                | STRING
                '''
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
  '''decl_item : decl
                | use_clause
                '''
  pass

#TODO grammar for use_clause
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
  pass

def p_def_id_s(t):
  '''def_id_s : def_id
              | def_id_s COMMA def_id
              '''
  pass

def p_def_id(t):
  'def_id  : IDENTIFIER'
  pass

def p_object_qualifier_opt(t):
  '''object_qualifier_opt :
                          | ALIASED
                          | CONSTANT
                          | ALIASED CONSTANT
                          '''
  pass

def p_object_subtype_def(t):
  '''object_subtype_def : subtype_ind
                        | array_type
                        '''
  pass

def p_init_opt(t):
  '''init_opt :
              | ASSIGNMENT expression
              '''
  pass

#grammar for number_decl
def p_number_decl(t):
  'number_decl : def_id_s COLON CONSTANT ASSIGNMENT expression SEMI_COLON'
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
  pass

def p_enumeration_type(t):
  'enumeration_type : BRA_OPEN enum_id_s BRA_CLOSE'
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

  pass
def p_range(t):
  '''range : simple_expression DOT_DOT simple_expression
          | name TICK RANGE
          | name TICK RANGE BRA_OPEN expression BRA_CLOSE
          '''
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
  pass

def p_unconstr_array_type(t):
  'unconstr_array_type : ARRAY BRA_OPEN index_s BRA_CLOSE OF component_subtype_def'
  pass

def p_index_s(t):
  '''index_s : index
            | index_s COMMA index
            '''
  pass

def p_index(t):
  'index : name RANGE BOX'
  pass

def p_component_subtype_def(t):
  'component_subtype_def : aliased_opt subtype_ind'
  pass

def p_aliased_opt(t):
  '''aliased_opt : 
                  | ALIASED
                  '''
  pass


def p_constr_array_type(t):
  'constr_array_type : ARRAY iter_index_constraint OF component_subtype_def'
  pass

def p_iter_index_constraint(t):
  'iter_index_constraint : BRA_OPEN iter_discrete_range_s BRA_CLOSE'
  pass

def p_iter_discrete_range_s(t):
  '''iter_discrete_range_s : discrete_range
                          | iter_discrete_range_s COMMA discrete_range
                          '''
  pass

def p_discrete_range(t):
  '''discrete_range : name range_constr_opt
                    | range
                    '''
  pass

#grammar for subtype_decl
def p_subtype_decl(t):
  'subtype_decl : SUBTYPE IDENTIFIER IS subtype_ind SEMI_COLON'
  pass

def p_subtype_ind(t):
  '''subtype_ind : name constraint
                  | name
                  '''
  pass

def p_constraint(t):
  '''constraint : range_constraint
                | decimal_digits_constraint
                '''
  pass

def p_decimal_digits_constraint(t):
  'decimal_digits_constraint : DIGITS expression range_constr_opt'
  pass

def p_range_constr_opt(t):
  '''range_constr_opt :
                      | range_constraint
                      '''
  pass


#grammar for subprog_decl
def p_subprog_decl(t):
  # not implemented generic_subp_inst, and subprog_spec IS ABSTRACT SEMI_COLON

  '''subprog_decl : subprog_spec SEMI_COLON
                  '''
  pass

def p_subprog_spec(t):
  '''subprog_spec : PROCEDURE compound_name formal_part_opt
                  | FUNCTION designator formal_part_opt RETURN name
                  | FUNCTION designator
                  '''
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

#TODO grammar for body
def p_body(t):
  'body : subprog_body'
  pass

def p_subprog_body(t):
  'subprog_body : subprog_spec IS decl_part block_body END id_opt SEMI_COLON'
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
          | operator_symbol
          '''
  pass

def p_name_opt(t):
  '''name_opt :
              | name
              '''
  pass

def p_simple_name(t):
  'simple_name : IDENTIFIER'
  pass

def p_indexed_comp(t):
  'indexed_comp : name BRA_OPEN value_s BRA_CLOSE'
  pass


def p_selected_comp(t):
  '''selected_comp : name DOT simple_name
                  | name DOT used_char
                  | name DOT operator_symbol
                  | name DOT ALL
                  '''
  pass

def p_used_char(t):
  'used_char : CHARACTER'
  pass

def p_operator_symbol(t):
  'operator_symbol : STRING'
  pass

def p_compound_name(t):
  '''compound_name : simple_name
                    | compound_name DOT simple_name
                    '''
  pass

#
def p_when_opt(t):
  '''when_opt :
              | WHEN condition
              '''
  pass

#grammar for value
def p_value_s(t):
  '''value_s : value
             | value_s COMMA value
             '''
  pass

def p_value(t):
  '''value : expression
           | comp_assoc
           | discrete_with_range
           | error
           '''
  pass

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

def p_discrete_with_range(t):
  '''discrete_with_range : name range_constraint
                          | range
                          '''
  pass

#TODO
def p_expression(t):
  'expression : '
  pass

#TODO
def p_qualified(t):
  'qualified : '
  pass

def p_simple_expression(t):
  'simple_expression :'
  pass
yacc.yacc()