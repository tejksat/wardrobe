from enum import Enum
from typing import Tuple, List

from .primitives import (
    Box,
    Point,
    Vector
)


class Side(Enum):
    X = 1
    Y = 2
    Z = 3
    iX = 4
    iY = 5
    iZ = 6


class Board(object):
    def __init__(self, box: Box) -> None:
        super().__init__()
        self.box = box
        self.cut_boxes = []

    def cut_corner(self, cut: List[Tuple[Side, float]]):
        assert len(cut) == 2

        epsilon = Vector(0.001, 0.001, 0.001)
        p0 = self.box.p0 - epsilon
        p1 = self.box.p1 + epsilon

        for c in cut:
            Board._adjust_side(p0, p1, c)

        self.cut_boxes.append(Box(p0, p1))

    @staticmethod
    def _adjust_side(p0: Point, p1: Point, side_length: Tuple[Side, float]):
        side, length = side_length

        if side == Side.X:
            p1.x = p0.x + length
        elif side == Side.Y:
            p1.y = p0.y + length
        elif side == Side.Z:
            p1.z = p0.z + length
        elif side == Side.iX:
            p0.x = p1.x - length
        elif side == Side.iY:
            p0.y = p1.y - length
        elif side == Side.iZ:
            p0.z = p1.z - length

    def get_corner_cut_boxes(self) -> List[Box]:
        return self.cut_boxes
