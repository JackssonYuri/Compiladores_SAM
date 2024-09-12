from grammar import Grammar
from predict import predict_algorithm
from token_sequence import token_sequence
from ll1_check import is_ll1

def print_grammar(G: Grammar) -> None:
    print('Terminais:', ' '.join([x for x in G.terminals()]))
    print('Não-terminais:', ' '.join([X for X in G.nonterminals()]))
    print('Produções:', ' '.join(
        ['id: ' + str(p) + ' ' + str(G.lhs(p)) + '->' + str(G.rhs(p)) for p in G.productions()]))

def create_example_grammar() -> Grammar:
    G = Grammar()
    G.add_nonterminal('S') 
    G.add_nonterminal('stmt')
    G.add_nonterminal('stmts')
    G.add_nonterminal('type')
    G.add_nonterminal('value')
    G.add_nonterminal('decl')
    G.add_nonterminal('decls')
    G.add_nonterminal('assignment')
    G.add_nonterminal('assign')
    G.add_nonterminal('attr')
    G.add_nonterminal('conditional')   
    G.add_nonterminal('loop')
    G.add_nonterminal('endcond')
    G.add_nonterminal('arithexp')
    G.add_nonterminal('binarymp')
    G.add_nonterminal('mpexp')
    G.add_nonterminal('binarytd')   
    G.add_nonterminal('tdexp')
    G.add_nonterminal('par')
    G.add_nonterminal('logicexp')
    G.add_nonterminal('orexp')
    G.add_nonterminal('<or>')
    G.add_nonterminal('andexp')
    G.add_nonterminal('<and>')
    G.add_nonterminal('factor')
    G.add_nonterminal('cmpexp')
    G.add_nonterminal('cmp')
    G.add_nonterminal('term') #28
      
    G.add_terminal('$')
    G.add_terminal('id')
    G.add_terminal('const')
    G.add_terminal('begin')
    G.add_terminal('end')
    G.add_terminal('main')
    G.add_terminal('print')
    G.add_terminal('int')
    G.add_terminal('float')
    G.add_terminal('if')
    G.add_terminal('else')
    G.add_terminal('end-if')
    G.add_terminal('while')
    G.add_terminal('end-while')
    G.add_terminal('+')
    G.add_terminal('-')
    G.add_terminal('*')
    G.add_terminal('/')
    G.add_terminal('=')
    G.add_terminal('+=')
    G.add_terminal('-=')
    G.add_terminal('*=')
    G.add_terminal('/=')
    G.add_terminal('and')
    G.add_terminal('or')
    G.add_terminal('not')
    G.add_terminal('equal')
    G.add_terminal('not-equal')
    G.add_terminal('greater')
    G.add_terminal('greater-equal')
    G.add_terminal('less')
    G.add_terminal('less-equal')
    G.add_terminal('(')
    G.add_terminal(')')
    G.add_terminal('->')

    G.add_production('S', ['begin', 'main', 'decls', 'stmts', 'end']) #63
    G.add_production('S', ['$'])  # id: 64
    G.add_production('decls', ['decl', 'decls'])  # id: 65
    G.add_production('decls', [])  # id: 66
    G.add_production('decl', ['type', 'id'])  # id: 66
    G.add_production('stmts', ['stmt', 'stmts'])  # id: 67
    G.add_production('stmts', [])  # id: 68
    G.add_production('stmt', ['print', 'value'])  # id: 69
    G.add_production('stmt', ['assignment'])  # id: 71
    G.add_production('stmt', ['conditional'])  # id: 72
    G.add_production('stmt', ['loop'])  # id: 73
    G.add_production('assignment', ['id', 'assign', 'arithexp'])  # id: 73
    G.add_production('conditional', ['if', 'logicexp', 'stmts', 'endcond'])  # id: 74
    G.add_production('endcond', ['end-if'])  # id: 75
    G.add_production('endcond', ['else', 'stmts', 'end-if'])  # id: 76
    G.add_production('loop', ['while', 'logicexp', 'stmts', 'end-while'])  # id: 77
    G.add_production('value', ['id'])  # id: 78
    G.add_production('value', ['const'])  # id: 79
    G.add_production('arithexp', ['binarymp'])  # id: 80
    G.add_production('binarymp', ['binarytd', 'mpexp'])  # id: 81
    G.add_production('mpexp', ['+', 'binarytd', 'mpexp'])  # id: 82
    G.add_production('mpexp', ['-', 'binarytd', 'mpexp'])  # id: 83
    G.add_production('mpexp', [])  # id: 84
    G.add_production('binarytd', ['par', 'tdexp'])  # id: 85
    G.add_production('tdexp', ['*', 'par', 'tdexp'])  # id: 86
    G.add_production('tdexp', ['/', 'par', 'tdexp'])  # id: 87
    G.add_production('tdexp', [])  # id: 88
    G.add_production('par', ['(', 'binarymp', ')'])  # id: 89
    G.add_production('par', ['value'])  # id: 90
    G.add_production('logicexp', ['orexp'])  # id: 91
    G.add_production('orexp', ['andexp', '<or>'])  # id: 92
    G.add_production('andexp', ['factor', '<and>'])  # id: 93
    G.add_production('factor', ['not', 'factor'])  # id: 94
    G.add_production('factor', ['(', 'orexp', ')'])  # id: 96
    G.add_production('factor', ['cmpexp'])  # id: 97
    G.add_production('assign', ['+'])  # id: 98
    G.add_production('assign', ['+=']) # id: 99
    G.add_production('assign', ['-=']) # id: 100
    G.add_production('assign', ['*=']) # id: 101
    G.add_production('assign', ['/=']) # id: 102
    G.add_production('type', ['int'])  # id: 103
    G.add_production('type', ['float'])  # id: 104
    G.add_production('<or>', ['or', 'andexp'])  # id: 105
    G.add_production('<or>', [])  # id: 106
    G.add_production('<and>', ['and', 'factor'])  # id: 107
    G.add_production('<and>', [])  # id: 108
    G.add_production('cmp', ['equal'])  # id: 109
    G.add_production('cmp', ['not-equal'])  # id: 110
    G.add_production('cmp', ['greater'])  # id: 111
    G.add_production('cmp', ['greater-equal'])  # id: 112
    G.add_production('cmp', ['less'])  # id: 113
    G.add_production('cmp', ['less-equal'])  # id: 114    
    G.add_production('term', ['cmp','value'])  # id: 115
    G.add_production('term', [])  # id: 115
    G.add_production('cmpexp', ['value', 'term'])  # id: 100
    
    return G

def S(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(63):
        print("Parsing S -> begin main decls stmts end")
        ts.match('begin')
        ts.match('main')
        decls(ts, p)
        stmts(ts, p)
        ts.match('end')
    elif ts.peek() in p.predict(64):
        print("Parsing S -> $")
        ts.match('$')

def decls(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(65):
        print("Parsing decls -> decl decls")
        decl(ts, p)
        decls(ts, p)
    elif ts.peek() in p.predict(66):
        print("Parsing decls -> ε")
        return

def decl(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(67):
        print("Parsing decl -> type id")
        type(ts, p)
        ts.match('id')   

def stmts(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(68):
        print("Parsing stmts -> stmt stmts")
        stmt(ts, p)
        stmts(ts, p)
    elif ts.peek() in p.predict(69):
        print("Parsing stmts -> ε")
        return

def stmt(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(70):
        print("Parsing stmt -> print value")
        ts.match('print')
        value(ts, p)
    elif ts.peek() in p.predict(71):
        print("Parsing stmt -> assignment")
        assignment(ts, p)
    elif ts.peek() in p.predict(72):
        print("Parsing stmt -> conditional")
        conditional(ts, p)
    elif ts.peek() in p.predict(73):
        print("Parsing stmt -> loop")
        loop(ts, p)

def assignment(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(74):
        print("Parsing assignment -> id assign arithexp")
        ts.match('id')
        print("Matched 'id', now parsing assign")
        assign(ts, p)
        print("Finished parsing assign, now parsing arithexp")
        arithexp(ts, p)
        print("Finished parsing arithexp")  

def conditional(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(75):
        print("Parsing conditional -> if logicexp stmts endcond")
        ts.match('if')
        logicexp(ts, p)
        stmts(ts, p)
        endcond(ts, p)

def endcond(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(76):
        print("Parsing endcond -> end-if")
        ts.match('end-if')
    elif ts.peek() in p.predict(77):
        print("Parsing endcond -> else stmts end-if")
        ts.match('else')
        stmts(ts, p)
        ts.match('end-if')

def loop(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(78):
        print("Parsing loop -> while logicexp stmts end-while")
        ts.match('while')
        logicexp(ts, p)
        stmts(ts, p)
        ts.match('end-while')

def value(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(79):
        print("Parsing value -> id")
        ts.match('id')
    elif ts.peek() in p.predict(80):
        print("Parsing value -> const")
        ts.match('const')

def arithexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(81):
        print("Parsing arithexp -> binarymp")
        binarymp(ts, p)   

def binarymp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(82):
        print("Parsing binarymp -> binarytd mpexp")
        binarytd(ts, p)
        mpexp(ts, p)   

def mpexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(83):
        print("Parsing mpexp -> + binarytd mpexp")
        ts.match('+')
        binarytd(ts, p)
        mpexp(ts, p)
    elif ts.peek() in p.predict(84):
        print("Parsing mpexp -> - binarytd mpexp")
        ts.match('-')
        binarytd(ts, p)
        mpexp(ts, p)
    elif ts.peek() in p.predict(85):
        print("Parsing mpexp -> ε")
        return    

def binarytd(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(86):
        print("Parsing binarytd -> par <tdexp>") 
        par(ts, p)
        tdexp(ts, p) 

def tdexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(87):
        print("Parsing binarytd -> * par  <tdexp>")
        ts.match('*')
        par(ts, p)
        tdexp(ts, p) 
                
    elif ts.peek() in p.predict(88):
        print("Parsing binarytd -> / par  <tdexp>")
        ts.match('/')
        par(ts, p)
        tdexp(ts, p) 
    elif ts.peek() in p.predict(89):
        print("Parsing binarytd -> ε")
        return
    
def par(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(90):
        print("Parsing par -> ( binarymp )")
        ts.match('(')
        binarymp(ts, p)
        ts.match(')')
    elif ts.peek() in p.predict(91):
        print("Parsing par -> value")
        value(ts, p)

def logicexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(92):
        print("Parsing logicexp -> orexp")
        orexp(ts, p)

def orexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(93):
        print("Parsing orexp -> andexp <or>")
        andexp(ts, p)
        #ts.match('or')
        or1(ts, p)

def andexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(94):
        print("Parsing andexp -> factor <and>")
        factor(ts, p)
        #ts.match('and')
        #andexp(ts, p)
        and1(ts, p)

def factor(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(95):
        print("Parsing factor -> not factor")
        ts.match('not')
        factor(ts, p)
    elif ts.peek() in p.predict(96):
        print("Parsing factor -> ( orexp )")
        ts.match('(')
        orexp(ts, p)
        ts.match(')')
    elif ts.peek() in p.predict(97):
        print("Parsing factor -> cmpexp")
        cmpexp(ts, p)

def assign(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(98):
        print("Parsing assign -> +")
        ts.match('+')
    elif ts.peek() in p.predict(99):
        print("Parsing assign -> +=")
        ts.match('+=')
    elif ts.peek() in p.predict(100):
        print("Parsing assign -> -=")
        ts.match('-=')
    elif ts.peek() in p.predict(101):
        print("Parsing assign -> *=")
        ts.match('*=')
    elif ts.peek() in p.predict(102):
        print("Parsing assign -> /=")
        ts.match('/=')
    else:
        print(f"Error: Unexpected token {ts.peek()} in assign")

def type(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(103):
        print("Parsing type -> int")
        ts.match('int')
    elif ts.peek() in p.predict(104):
        print("Parsing type -> float")
        ts.match('float')

def or1(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(105):
        print("Parsing or -> or andexp")
        ts.match('or')
        andexp(ts, p)
    elif ts.peek() in p.predict(106):
        print("Parsing or -> ε")
        return
    
def and1(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(107):
        print("Parsing or -> and factor")
        ts.match('and')
        factor(ts, p)
    elif ts.peek() in p.predict(108):
        print("Parsing or -> ε")
        return
    
def cmp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(109):
        print("Parsing cmp -> equal")
        ts.match('equal')
    elif ts.peek() in p.predict(110):
        print("Parsing cmp -> not-equal")
        ts.match('not-equal')
    elif ts.peek() in p.predict(111):
        print("Parsing cmp -> greater")
        ts.match('greater')
    elif ts.peek() in p.predict(112):
        print("Parsing cmp -> greater-equal")
        ts.match('greater-equal')
    elif ts.peek() in p.predict(113):
        print("Parsing cmp -> less")
        ts.match('less')
    elif ts.peek() in p.predict(114):
        print("Parsing cmp -> less-equal")
        ts.match('less-equal')

def cmpexp(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(117):
        print("Parsing cmpexp -> value term term")
        value(ts, p)
        term(ts, p)

def term(ts: token_sequence, p: predict_algorithm) -> None:
    if ts.peek() in p.predict(115):
        print("Parsing term -> value")
        ts.match('value')
    elif ts.peek() in p.predict(116):
        print("Parsing term -> ε")
        return

if __name__ == '__main__':
    G = create_example_grammar()
    print_grammar(G)
    predict_alg = predict_algorithm(G)
    ts = token_sequence(['begin', 'main', 'id', '+', 'id', 'end', '$'])
    S(ts, predict_alg)
    ll1_result = is_ll1(G, predict_alg)
    print(f"A gramática é LL(1)? {ll1_result}")
