import corner_measures
# TODO fix this strange import
from builder.boards import Board, Side
from builder.primitives import Box, Point
from builder.wardrobe_builder import WardrobeBuilder
from wardrobe import plinth, bottom, top
from .constants import (
    LEFT_PART_WIDTH,
    RIGHT_PART_WIDTH,
    SIDE_THICKNESS,
    LEFT_SIDE_DEPTH,
    RIGHT_SIDE_DEPTH
)


def build(builder: WardrobeBuilder):
    """
    Build the corner part of the wardrobe
    """

    # build starting from the left wall with X axis pointing to the origin
    builder.set_origin(x0=0, y0=0, z0=0, x1=-1, y1=1, z1=1)
    builder.use_XYZ()

    # build left side
    builder.add_board(x=LEFT_PART_WIDTH,
                      y=0,
                      z=0,
                      width=SIDE_THICKNESS,
                      height=corner_measures.HEIGHT,
                      depth=LEFT_SIDE_DEPTH)

    # build right side
    builder.add_board(x=0,
                      y=0,
                      z=RIGHT_PART_WIDTH,
                      width=RIGHT_SIDE_DEPTH,
                      height=corner_measures.HEIGHT,
                      depth=SIDE_THICKNESS)

    # plinth and top constants
    # TODO what is the constant for 0.6?
    x_cut = LEFT_PART_WIDTH - 0.6
    z_cut = RIGHT_PART_WIDTH - 0.6

    # build plinth
    plinth_board = Board(Box(Point(0, plinth.PLINTH_HEIGHT, 0),
                             Point(LEFT_PART_WIDTH, plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
                                   RIGHT_PART_WIDTH)))
    plinth_board.cut_corner([(Side.iX, x_cut), (Side.iZ, z_cut)])
    builder.add_board_object(plinth_board)

    # build top
    top_board = Board(Box(Point(0, corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS, 0),
                          Point(LEFT_PART_WIDTH, corner_measures.HEIGHT, RIGHT_PART_WIDTH)))
    top_board.cut_corner([(Side.iX, x_cut), (Side.iZ, z_cut)])
    builder.add_board_object(top_board)
