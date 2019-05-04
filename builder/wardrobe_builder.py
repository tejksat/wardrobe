from typing import List

import numpy as np

from builder.boards import Board
from builder.primitives import Box, Point


class WardrobeBuilder(object):
    def __init__(self) -> None:
        self.origin_vector = np.array([0, 0, 0])
        self.axis_vector = np.array([1, 1, 1])
        self.transform_matrix = np.array([[1, 0, 0],
                                          [0, 1, 0],
                                          [0, 0, 1]])

    def set_origin(self, x0, y0, z0, x1, y1, z1):
        self.origin_vector = np.array([x0, y0, z0])
        self.axis_vector = np.array([x1, y1, z1])

    def use_XYZ(self):
        self.transform_matrix = np.array([[1, 0, 0],
                                          [0, 1, 0],
                                          [0, 0, 1]])

    def use_iXYZ(self):
        """
        Use inverted X-axis and original Y- and Z-axises.
        """
        self.transform_matrix = np.array([[-1, 0, 0],
                                          [0, 1, 0],
                                          [0, 0, 1]])

    def use_ZYiX(self):
        """
        Use Z-axis as X-axis, original Y-axis, and inverted X-axis as Z-axis.
        """
        self.transform_matrix = np.array([[0, 0, -1],
                                          [0, 1, 0],
                                          [1, 0, 0]])

    def _to_absolute_vector(self, v) -> List[float]:
        return self.origin_vector + (v.T @ self.transform_matrix)

    def _to_absolute_point(self, p) -> Point:
        absolute_vector = self._to_absolute_vector(np.array([p.x, p.y, p.z]))
        return Point(absolute_vector[0], absolute_vector[1], absolute_vector[2])

    def _to_absolute_box(self, box: Box) -> Box:
        p0 = self._to_absolute_point(box.p0)
        p1 = self._to_absolute_point(box.p1)
        return Box(p0, p1)

    def add_board(self, x, y, z, width, height, depth):
        raise NotImplementedError

    def add_board_object(self, board: Board):
        raise NotImplementedError
