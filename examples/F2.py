from vectorfield import *

def f(p: Point) -> 'Vector':
    return Vector(-p.y, p.x)

F = Field(f, 100, 100, 10)

F.prepare()

F.normalize()

F.draw()
