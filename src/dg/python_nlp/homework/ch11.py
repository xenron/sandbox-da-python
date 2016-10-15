# -*- coding: utf-8 -*-

# 《Python自然语言处理》第10章课后习题
# 1，2，3

import nltk

# 1. Translate the following sentences into propositional logic and verify that they parse with LogicParser.
# Provide a key that shows how the propositional variables in your translation correspond to expressions of English.
# 1. 将下列句子翻译成命题逻辑，并用LogicParser 验证结果。
# 提供显示你的翻译中命题变量如何对应英语表达的一个要点。
# a. If Angus sings, it is not the case that Bertie sulks.
# b. Cyril runs and barks.
# c. It will snow if it doesn’t rain.
# d. It’s not the case that Irene will be happy if Olive or Tofu comes.
# e. Pat didn’t cough or sneeze.
# f. If you don’t come if I call, I won’t come if you call.

##命题逻辑
nltk.boolean_ops()

read_expr = nltk.sem.Expression.fromstring
# a. If Angus sings, it is not the case that Bertie sulks.
read_expr(r'sing(angus) -> ~sulk(bertie)')

# b. Cyril runs and barks.
read_expr(r'run(cyril) & bark(cyril)')

# c. It will snow if it doesn't rain.
read_expr(r'~rain -> snow')

# d. It's not the case that Irene will be happy if Olive or Tofu comes.
# read_expr(r'~( (come(olive) | come(tofu)) -> happy(irene) )')
read_expr(r'~(( (come(olive) | come(tofu)) -> happy(irene) ))')
read_expr(r'~(( (come(olive) | come(tofu)) -> happy(irene) ))')

# e. Pat didn't cough or sneeze.
read_expr(r'~((cough(pat) | sneeze(pat)))')

# f. If you don't come if I call, I won't come if you call.
read_expr(r'((call(i,you) -> ~come(you)) -> (call(you,i) -> ~come(i)))')

# 2. Translate the following sentences into predicate-argument formulas of first-order logic.
# 2. 翻译下面的句子为一阶逻辑的谓词参数公式。
# a. Angus likes Cyril and Irene hates Cyril.
# b. Tofu is taller than Bertie.
# c. Bruce loves himself and Pat does too.
# d. Cyril saw Bertie, but Angus didn’t.
# e. Cyril is a four-legged friend.
# f. Tofu and Olive are near each other.

# a. Angus likes Cyril and Irene hates Cyril.
like(angus,cyril) & hate(irene,cyril)
# b. Tofu is taller than Bertie.
is_taller(tofu, bertie)
# c. Bruce loves himself and Pat does too.
love(bruce,bruce) & love(pat, pat)
# d. Cyril saw Bertie, but Angus didn't.
saw(cyril, bertie) & ~( saw(angus, bertie) )
# e. Cyril is a four-legged friend.
four_legged(cyril) & friend(cyril)
# f. Tofu and Olive are near each other.
near(tofu, olive) & near(olive, tofu)

# 3. Translate the following sentences into quantified formulas of first-order logic.
# 3. 翻译下列句子为成一阶逻辑的量化公式。
# a. Angus likes someone and someone likes Julia.
# b. Angus loves a dog who loves him.
# c. Nobody smiles at Pat.
# d. Somebody coughs and sneezes.
# e. Nobody coughed or sneezed.
# f. Bruce loves somebody other than Bruce.
# g. Nobody other than Matthew loves Pat.
# h. Cyril likes everyone except for Irene.
# i. Exactly one person is asleep.

# a. Angus likes someone and someone likes Julia.
exists x.(like(angus, x)) & exists y.(like(y,julia))
# b. Angus loves a dog who loves him.
exists x.(dog(x) & love(angus, x) & love(x,angus))
# c. Nobody smiles at Pat.
~(exists x.(smile(x,pat)))
# d. Somebody coughs and sneezes.
exists x.(coughs(x) & sneeze(x))
# e. Nobody coughed or sneezed.
~(exists x.(coughs(x) | sneeze(x)))
# f. Bruce loves somebody other than Bruce.
exists x.(love(bruce, x) & x != bruce)
# g. Nobody other than Matthew loves Pat.
all x.(~(love(x,pat) | x = matthew)) & love(matthew,pat)
# h. Cyril likes everyone except for Irene.
all x.(like(cyril, x) | x = irene) & ~(like(cyril, irene))
# i. Exactly one person is asleep.
exists x.(asleep(x) & all y.(asleep(y) -> y=x))
