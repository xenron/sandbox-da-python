# -*- coding: utf-8 -*-

import nltk

##基于sql数据库的问答系统
nltk.data.show_cfg('grammars/book_grammars/sql0.fcfg')

from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)

from nltk.sem import chat80
rows = chat80.sql_query('corpora/city_database/city.db', q)
for r in rows: 
    print(r[0]," ")


##命题逻辑
nltk.boolean_ops()

read_expr = nltk.sem.Expression.fromstring
read_expr('-(P & Q)')

read_expr('P & Q')

read_expr('P | (R -> Q)')

read_expr('P <-> -- P')

lp = nltk.sem.Expression.fromstring
SnF = read_expr('SnF')
NotFnS = read_expr('-FnS')
R = read_expr('SnF -> -FnS')
prover = nltk.Prover9()
prover.config_prover9(r'D:\Program Files\LADR1007B-win\bin')
prover.prove(NotFnS, [SnF, R])


val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
val['P']

dom = set()
g = nltk.Assignment(dom)

m = nltk.Model(dom, val)

print(m.evaluate('(P & Q)', g))
print(m.evaluate('-(P & Q)', g))
print(m.evaluate('(P & R)', g))
print(m.evaluate('(P | R)', g))

##一阶逻辑
read_expr = nltk.sem.Expression.fromstring
expr = read_expr('walk(angus)', type_check=True)
expr.argument

expr.argument.type

expr.function

expr.function.type

sig = {'walk': '<e, t>'}
expr = read_expr('walk(angus)', signature=sig)
expr.function.type

read_expr = nltk.sem.Expression.fromstring
read_expr('dog(cyril)').free()

read_expr('dog(x)').free()

read_expr('own(angus, cyril)').free()

read_expr('exists x.dog(x)').free()

read_expr('((some x. walk(x)) -> sing(x))').free()

read_expr('exists x.own(y, x)').free()

#真值模型
dom = {'b', 'o', 'c'}
v = """
bertie => b
olive => o
cyril => c
boy => {b}
girl => {o}
dog => {c}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
"""
val = nltk.Valuation.fromstring(v)
print(val)

('o', 'c') in val['see']

('b',) in val['boy']

#运算
g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
g

print(g)

m = nltk.Model(dom, val)
m.evaluate('see(olive, y)', g)

g['y']

m.evaluate('see(y, x)', g)

g.purge()
g

m.evaluate('see(olive, y)', g)
 
m.evaluate('see(bertie, olive) & boy(bertie) & -walk(bertie)', g)

##量化
m.evaluate('exists x.(girl(x) & walk(x))', g)

m.evaluate('girl(x) & walk(x)', g.add('x', 'o'))

fmla1 = read_expr('girl(x) | boy(x)')
m.satisfiers(fmla1, 'x', g)
fmla2 = read_expr('girl(x) -> walk(x)')
m.satisfiers(fmla2, 'x', g)
fmla3 = read_expr('walk(x) -> girl(x)')
m.satisfiers(fmla3, 'x', g)

m.evaluate('all x.(girl(x) -> walk(x))', g)

##量词歧义
v2 = """
bruce => b
elspeth => e
julia => j
matthew => m
person => {b, e, j, m}
admire => {(j, b), (b, b), (m, e), (e, m)}
"""
val2 = nltk.Valuation.fromstring(v2)


dom2 = val2.domain
m2 = nltk.Model(dom2, val2)
g2 = nltk.Assignment(dom2)
fmla4 = read_expr('(person(x) -> exists y.(person(y) & admire(x, y)))')
m2.satisfiers(fmla4, 'x', g2)

fmla5 = read_expr('(person(y) & all x.(person(x) -> admire(x, y)))')
m2.satisfiers(fmla5, 'y', g2)

fmla6 = read_expr('(person(y) & all x.((x = bruce | x = julia) -> admire(x, y)))')
m2.satisfiers(fmla6, 'y', g2)



##句子语义理解
read_expr = nltk.sem.Expression.fromstring
expr = read_expr(r'\x.(walk(x) & chew_gum(x))')
expr

expr.free()

print(read_expr(r'\x.(walk(x) & chew_gum(y))'))

expr = read_expr(r'\x.(walk(x) & chew_gum(x))(gerald)')
print(expr)
print(expr.simplify()) 

print(read_expr(r'\x.\y.(dog(x) & own(y, x))(cyril)').simplify())
print(read_expr(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify())


expr1 = read_expr('exists x.P(x)')
print(expr1)

expr2 = expr1.alpha_convert(nltk.sem.Variable('z'))
print(expr2)

expr1 == expr2

expr3 = read_expr('\P.(exists x.P(x))(\y.see(y, x))')
print(expr3)

print(expr3.simplify())

##量词歧义
from nltk.sem import cooper_storage as cs
sentence = 'every girl chases a dog'
trees = cs.parse_with_bindops(sentence, grammar='grammars/book_grammars/storage.fcfg')
semrep = trees[0].label()['SEM']
cs_semrep = cs.CooperStore(semrep)
print(cs_semrep.core)

for bo in cs_semrep.store:
        print(bo)
        
cs_semrep.s_retrieve(trace=True)

for reading in cs_semrep.readings:
       print(reading)      
       
#段落语义理解
read_dexpr = nltk.sem.DrtExpression.fromstring
drs1 = read_dexpr('([x, y], [angus(x), dog(y), own(x, y)])')
print(drs1)      

drs1.draw()

print(drs1.fol())       

drs2 = read_dexpr('([x], [walk(x)]) + ([y], [run(y)])')
print(drs2)

print(drs2.simplify())

drs3 = read_dexpr('([], [(([x], [dog(x)]) -> ([y],[ankle(y), bite(x, y)]))])')
print(drs3.fol())
        

drs4 = read_dexpr('([x, y], [angus(x), dog(y), own(x, y)])')
drs5 = read_dexpr('([u, z], [PRO(u), irene(z), bite(u, z)])')
drs6 = drs4 + drs5
print(drs6.simplify())

print(drs6.simplify().resolve_anaphora())

from nltk import load_parser
parser = load_parser('grammars/book_grammars/drt.fcfg', logic_parser=nltk.sem.drt.DrtParser())
trees = list(parser.parse('Angus owns a dog'.split()))
print(trees[0].label()['SEM'].simplify())

    