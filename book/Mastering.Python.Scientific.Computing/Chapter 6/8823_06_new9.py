from sympy import Symbol, Interval
from sympy import FiniteSet

Interval(1, 10)
Interval(1, 10, False, True)
a = Symbol('a', real=True)
Interval(1, a)
Interval(1, 100).end
from sympy import Interval
Interval(0, 1).start

Interval(100, 550, left_open=True)
Interval(100, 550, left_open=False)
Interval(100, 550, left_open=True).left_open
Interval(100, 550, left_open=False).left_open

Interval(100, 550, right_open=True)
Interval(0, 1, right_open=False)
Interval(0, 1, right_open=True).right_open
Interval(0, 1, right_open=False).right_open


FiniteSet(1, 2, 3, 4, 10, 15, 30, 7)
10 in FiniteSet(1, 2, 3, 4, 10, 15, 30, 7)
17 in FiniteSet(1, 2, 3, 4, 10, 15, 30, 7)