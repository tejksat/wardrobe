from builder.boards import Board
from builder.primitives import Box, Point
from builder.wardrobe_builder import WardrobeBuilder
from common import mdf

SHELF_BOARD_THICKNESS = mdf.STANDARD

HORIZONTAL_OFFSETS = 0.01
"""
Offsets from right and left boards for runners
"""

BOTTOM_OFFSET = 0.01

TOP_OFFSET = 0.01

FACADE_THICKNESS = 0.02

BACK_OFFSET = 0.02
"""
Technical offset from the back of the wardrobe.
"""


def build_shelf(builder: WardrobeBuilder, box: Box):
    """
    Builds shelf inside the region described by the `box`.

    The facade is in XY plane and it facing towards the greater Z.

    - Left and right sides are full-length.
    - The back and the front are between left and right sides.
    - Bottom is between left, right, back and front.
    """
    p0 = box.p0 + Point(HORIZONTAL_OFFSETS, BACK_OFFSET, BOTTOM_OFFSET)
    p1 = box.p1 - Point(HORIZONTAL_OFFSETS, FACADE_THICKNESS, TOP_OFFSET)

    # left side
    builder.add_board_object(Board(Box(p0, Point(p0.x + SHELF_BOARD_THICKNESS, p1.y, p1.z))))

    # right side
    builder.add_board_object(Board(Box(Point(p1.x - SHELF_BOARD_THICKNESS, p0.y, p0.z), p1)))

    # back side
    builder.add_board_object(Board(Box(
        Point(p0.x + SHELF_BOARD_THICKNESS, p0.y, p0.z),
        Point(p1.x, p1.y, p0.z + SHELF_BOARD_THICKNESS)
    )))

    # front side
    builder.add_board_object(Board(Box(
        Point(p0.x + SHELF_BOARD_THICKNESS, p0.y, p1.z - SHELF_BOARD_THICKNESS),
        Point(p1.x, p1.y, p1.z)
    )))

    # bottom
    builder.add_board_object(Board(Box(
        Point(p0.x + SHELF_BOARD_THICKNESS, p0.y, p0.z + SHELF_BOARD_THICKNESS),
        Point(p1.x - SHELF_BOARD_THICKNESS, p0.y + SHELF_BOARD_THICKNESS, p1.z)
    )))
