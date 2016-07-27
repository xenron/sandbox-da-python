from sympy import FiniteSet, Intersection, Interval,  ProductSet, Union
init_printing(use_unicode=False, wrap_line=False, no_global=True)

Union(Interval(1, 10), Interval(10, 30))
Union(Interval(5, 15), Interval(15, 25))
Union(FiniteSet(1, 2, 3, 4), FiniteSet(10, 15, 30, 7))

Intersection(Interval(1, 3), Interval(2, 4))
Interval(1,3).intersect(Interval(2,4))
Intersection(FiniteSet(1, 2, 3, 4), FiniteSet(1, 3, 4, 7))
FiniteSet(1, 2, 3, 4).intersect(FiniteSet(1, 3, 4, 7))

I = Interval(0, 5)
S = FiniteSet(1, 2, 3)
ProductSet(I, S)
(2, 2) in ProductSet(I, S)

Interval(0, 1) * Interval(0, 1) 
coin = FiniteSet('H', 'T')
set(coin**2)

Complement(FiniteSet(0, 1, 2, 3, 4, 5), FiniteSet(1, 2))
