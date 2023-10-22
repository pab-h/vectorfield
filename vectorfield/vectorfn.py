from typing import Callable

from vectorfield.point import Point
from vectorfield.vector import Vector

VectorFn = Callable[[Point], Vector]
