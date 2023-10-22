from typing import Union

from turtle import Turtle

from vectorfield.point import Point

from math import atan2
from math import sqrt
from math import pow
from math import pi

class Vector:
    def __init__(self, vx: float, vy: float) -> None:
        self.vx = vx
        self.vy = vy
        self.color = "cyan"
        self.head_size = 5

    def __repr__(self) -> str:
        return f"V({ self.vx }, { self.vy })"

    def __mul__(self, other: Union[float, int]) -> 'Vector':
        v = Vector(self.vx * other, self.vy * other)
        v.color = self.color

        return v
    
    def __add__(self, other: 'Vector') -> 'Vector':
        v = Vector(self.vx + other.vx, self.vy + other.vy)
        v.color = self.color

        return v
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        v = Vector(self.vx - other.vx, self.vy - other.vy)
        v.color = self.color
        
        return v

    @property
    def angle(self) -> float:
        return atan2(self.vy, self.vx) * 180 / pi

    @property
    def module(self) -> float:
        return sqrt(pow(self.vx, 2) + pow(self.vy, 2))

    def normalize(self) -> 'Vector':
        module = self.module

        if module == 0:
            return self

        return self * (1 / module)

    def draw(self, t: Turtle, target: Point) -> None:

        t.penup()

        t.setx(target.x)
        t.sety(target.y)

        t.pendown()

        t.color(self.color)
        t.fillcolor(self.color)

        t.setheading(self.angle)
        t.forward(self.module)

        t.begin_fill()

        t.left(90)
        t.forward(self.head_size)

        t.right(120)
        t.forward(self.head_size * 2)

        t.right(120)
        t.forward(self.head_size * 2)

        t.right(120)
        t.forward(self.head_size)

        t.end_fill()
