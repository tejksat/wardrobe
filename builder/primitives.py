from typing import List


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def as_list(self) -> List[float]:
        return [self.x, self.y, self.z]

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Point(other * self.x, other * self.y, other * self.z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)


class Box(object):
    def __init__(self, p0: Point, p1: Point):
        super().__init__()
        # todo normalize to lowest coordinates for p0 and highest for p1
        self.p0 = p0
        self.p1 = p1


def create_box(x: float, y: float, z: float, width: float, height: float, depth: float) -> Box:
    p0 = Point(x, y, z)
    p1 = p0 + Point(width, height, depth)
    return Box(p0, p1)
