from vectorfield import *

import math

def f(p: Point) -> 'Vector':
    return Vector(p.x * math.cos(p.y), p.y * math.sin(p.x))

F = Field(f, 100, 100, 10)

F.prepare()

F.normalize(5)

F.draw()
