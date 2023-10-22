from turtle import Turtle
from turtle import Screen

from vectorfield.vectorfn import VectorFn
from vectorfield.vector import Vector
from vectorfield.point import Point

class Field:
    def __init__(self, fn: VectorFn, rows: int, columns: int, gap: int) -> None:
        self.screen = Screen()
        self.screen.bgcolor("black")

        self.t = Turtle()
        self.t.hideturtle()
        self.t.speed(0)

        self.fn = fn
        self.rows = rows
        self.columns = columns
        self.gap = gap

        self.vectors: list[Vector] = []
        self.grid: list[Point] = []

    def __add__(self, other: "Field") -> "Field":
        def f(p: Point) -> "Vector":
            return self.fn(p) + other.fn(p)

        F = Field(f, self.rows, self.columns, self.gap)

        F.grid = self.grid

        for v1, v2 in zip(self.vectors, other.vectors):
            F.vectors.append(v1 + v2)

        return F

    def prepare(self) -> None:
        self.init_grid()
        self.init_vectors()

    def init_grid(self) -> None: 
        for x in range(-self.columns, self.columns, self.gap):
            for y in range(-self.rows, self.rows, self.gap):
                self.grid.append(Point(x, y))

    def init_vectors(self) -> None:
        self.vectors.clear()

        for point in self.grid:
            self.vectors.append(self.fn(point))

    def scale_color(self, module: float) -> str:
        min_module = min(self.vectors, key = lambda v: v.module).module
        max_module = max(self.vectors, key = lambda v: v.module).module

        if max_module == min_module:
            return "black"

        z = (module - min_module) / (max_module - min_module)

        min_color = (0, 0, 255)
        max_color = (255, 0, 0)

        color = (
            int(min_color[0] + z * (max_color[0] - min_color[0])),
            int(min_color[1] + z * (max_color[1] - min_color[1])),
            int(min_color[2] + z * (max_color[2] - min_color[2]))
        )

        color = tuple(max(0, min(255, x)) for x in color)

        return "#{:02X}{:02X}{:02X}".format(*color)

    def normalize(self, scale: float = 25) -> None:
        for i, v in enumerate(self.vectors):
            module = v.module

            self.vectors[i] = v.normalize() * scale
            self.vectors[i].color = self.scale_color(module)

    def draw(self) -> None:
        for v, p in zip(self.vectors, self.grid):
            v.draw(self.t, p)

        self.screen.exitonclick()
