from typing import List, TextIO

import numpy as np

from .boards import Board
from .primitives import Box
from .wardrobe_builder import WardrobeBuilder


def _pov_ray_point(v: List[float]):
    return f'<{v[0]}, {v[1]}, {v[2]}>'


def _pov_ray_box(v1: List[float], v2: List[float], texture: str = None):
    extra_box_info = ''
    if texture:
        extra_box_info = f' texture {{{texture}}}'
    return f'box {{ {_pov_ray_point(v1)}, {_pov_ray_point(v2)}{extra_box_info}}}\n'


def _pov_ray_box_object(box: Box, texture: str = None):
    return _pov_ray_box(box.p0.as_list(), box.p1.as_list(), texture)


class PovBuilder(WardrobeBuilder):
    def __init__(self, writer: TextIO) -> None:
        super().__init__()
        self.writer = writer

    def add_board(self, x, y, z, width, height, depth):
        v1 = self._to_absolute_vector(np.array([x, y, z]))
        v2 = self._to_absolute_vector(np.array([x + width, y + height, z + depth]))

        self.writer.write(_pov_ray_box(v1, v2, texture='Texture_01'))

    def add_board_object(self, board: Board):
        cut_boxes = board.get_corner_cut_boxes()
        if cut_boxes:
            self.writer.write('difference {\n')
            self.writer.write(_pov_ray_box_object(self._to_absolute_box(board.box), texture='Texture_01'))
            for cut_box in cut_boxes:
                self.writer.write(_pov_ray_box_object(self._to_absolute_box(cut_box)))
            self.writer.write('cutaway_textures\n')
            self.writer.write('}\n')
        else:
            self.writer.write(_pov_ray_box_object(self._to_absolute_box(board.box), texture='Texture_01'))

    def build(self):
        pass
