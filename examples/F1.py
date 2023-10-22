from vectorfield import *

def f(p: Point) -> 'Vector':
    return Vector(p.x, p.y)

F = Field(f, 100, 100, 10)

F.prepare()

F.normalize()

F.draw()
