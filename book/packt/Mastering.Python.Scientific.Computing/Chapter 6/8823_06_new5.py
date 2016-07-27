from sympy import *
from sympy.geometry import *

x = Point(0, 0)
y = Point(1, 1)
z = Point(2, 2)
zp = Point(1, 0)

Point.is_collinear(x, y, z)
Point.is_collinear(x, y, zp)

t = Triangle(zp, y, x)
t.area
t.medians[x]

Segment(Point(1, S(1)/2), Point(0, 0))
m = t.medians
intersection(m[x], m[y], m[zp])

c = Circle(x, 5)
l = Line(Point(5, -5), Point(5, 5))
c.is_tangent(l)
l = Line(x, y)
c.is_tangent(l)
intersection(c, l)

c1 = Circle( Point(2,2), 7)
c1.circumference()
c1.equation()
l1 = Line (Point (0,0), Point(10,10))
intersection (c1,l1)
