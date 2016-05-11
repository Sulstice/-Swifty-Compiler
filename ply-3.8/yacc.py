from lex import tokens

# BNF Parsing rules

alist = []
names = {}

DEBUG = True

def p_program(p):
    '''program : declarations
               | functions
               | declarations functions'''
    print ("Saw a program")

def p_functions(p):
    '''functions : function
                 | functions function'''

def p_function(p):
    '''function : FUNC IDENTIFIER LPAREN RPAREN MAP_TO type LCURLY RCURLY
                | FUNC IDENTIFIER LPAREN RPAREN MAP_TO type LCURLY declarations RCURLY
                | FUNC IDENTIFIER LPAREN RPAREN MAP_TO type LCURLY declarations statements RCURLY'''

    print ("Saw a function")
    
def p_declarations(p):
    '''declarations : type idList SEMI
               | declarations type idList SEMI
               | type idList EQUALS expression SEMI
               | declarations type idList EQUALS expression SEMI'''
    if len(p)   == 4 : p[0] = p[2]
    elif len(p) == 5 : p[0] = p[3]
    elif len(p) == 6 : p[0] = p[2] + " = " + p[4]
    elif len(p) == 7 : p[0] = p[3] + " = " + p[5]
    print ("Saw a declaration")

def p_idList(p):
    '''idList : IDENTIFIER
              | IDENTIFIER COMMA idList
              | INTEGER
              | INTEGER COMMA idList'''
    if len(p) == 2: p[0] = p[1]
    else: p[0] = str(p[1]) + " , " + str(p[3])

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | LIST
            | TUPLE
            | OBJECT
            | STRING'''

def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : expression SEMI
                 | assignment SEMI
                 | whileStatement
                 | listStatement
                 | streamStatement
                 | arrayStatement
                 | filterStatement
                 '''

def p_assignment(p):
    '''assignment : LET IDENTIFIER EQUALS expression SEMI'''
    p[0] = "Assignment"
    names[p[2]] = p[4]

def p_while(p):
    '''whileStatement : WHILE LPAREN expression RPAREN LCURLY statements RCURLY'''
    p[0] = "While"
    print ("Saw a While Statement")

def p_list(p):
    '''listStatement  : LET IDENTIFIER EQUALS LBRACE idList RBRACE SEMI
                      | LET IDENTIFIER EQUALS LBRACE RBRACE SEMI'''
    p[0] = "List"
    idList = p[5]
    names[p[2]] = p[5]
    for i in idList.split(","):
        d = int(i)
        alist.append(d)

    print ("Saw a List Statement")

def p_filter(p):
    '''filterStatement : FILTER LCURLY LT_OP INTEGER GT_OP PRCNT INTEGER EQ_OP INTEGER RCURLY'''
    a = p[7]
    b = p[9]
    p[0] = lambda (x): x % a == b

    print ("Saw a Filter Statement")

def p_streamOperation(p):
    '''streamStatement : IDENTIFIER PIPE STREAM LPAREN RPAREN SEMI'''
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s''" % p[1])
        p[0]

    print ("Saw a Stream Statement")
    from java.util import Arrays
    from java.util import List
    import Stream
    newString = "Calling Stream Operation Result: "
    print (newString)
    Stream.streamOperation(alist)
    print ("")

def p_openrange(p):
    '''arrayStatement : LET IDENTIFIER EQUALS ARRAY LPAREN INTEGER OPEN_RNG INTEGER RPAREN PIPE filterStatement'''
    arrayList = []
    daRange = p[8] - p[6] - 1
    for item in range(daRange):
         if p[11](item):
            arrayList.append(item)

    print ("Saw an Array Statement")

    print (arrayList)
    
def p_expression(p):
    '''expression : conjunction
                  | conjunction OR_OP expression'''
    p[0] = "Expression: ", p[1]

def p_conjunction(p):
    '''conjunction : equality
                   | AND_OP equality'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_equality(p):
    '''equality : relation
                | relation equOp equality'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_equOp(p):
    '''equOp : EQ_OP
             | NE_OP'''
    p[0] = p[1]

def p_relation(p):
    '''relation : addition
                | addition relOp relation'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_relOp(p):
    '''relOp : LT_OP
             | LE_OP
             | GT_OP
             | GE_OP'''
    p[0] = p[1]

def p_addition(p):
    '''addition : term
                | term addOP addition'''
    if len (p) == 4:
        p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else:
        p[0] = p[1]

def p_addOP(p):
    '''addOP : PLUS
             | MINUS'''
    p[0] = p[1]

def p_term(p):
    '''term : factor
            | factor mulOP term'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = p[1]

def p_mulOP(p):
    '''mulOP : MULT
             | DIV
             | PRCNT'''
    p[0] = p[1]

def p_factor(p):
    '''factor : primary
              | primary unaryOP factor'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = p[1]

def p_unaryOp(p):
    '''unaryOP : MINUS
               | BANG'''
    p[0] = p[1]

def p_primary(p):
    '''primary : literal'''
    p[0] = p[1]

def p_literal(p):
    '''literal : INTEGER
               | IDENTIFIER
               | TRUE
               | FALSE
               | CLFLOAT
               | CLSTRING'''
    p[0] = p[1]

def emptyline(self):
    """Do nothing on empty input line"""
    pass# Error handling rule

def p_error(p):
    print ("At line: ", p.lexer.lineno)
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

with open('function.txt', 'r') as content_file:
    content = content_file.read()
yacc.parse(content)

