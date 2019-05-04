import corner_measures
from builder import volumes, primitives
from builder.boards import Board
from builder.shelves import build_shelf
from builder.wardrobe_builder import WardrobeBuilder
from wardrobe import plinth, bottom, top
from wardrobe.right_part.constants import LEFT_SIDE_DEPTH
from .constants import (
    WIDTH,
    RIGHT_SIDE_DEPTH,
    RIGHT_SIDE_HEIGHT,
    RIGHT_SIDE_THICKNESS,
    LEFT_SIDE_THICKNESS,
    LEFT_SIDE_HEIGHT,
    SECTION_THICKNESS,
    RIGHT_SECTION_WIDTH,
    LEFT_SECTION_WIDTH
)

# todo move to constants
SHELF_HEIGHT = 0.2
BIG_SHELF_HEIGHT = 0.4


def build(builder: WardrobeBuilder):
    # build starting from the right wall with Y axis pointing to the origin
    builder.set_origin(x0=0, y0=0, z0=corner_measures.RIGHT_WALL, x1=1, y1=1, z1=-1)
    builder.use_ZYiX()

    # build right side
    builder.add_board(x=0, y=0, z=0, width=RIGHT_SIDE_THICKNESS, height=RIGHT_SIDE_HEIGHT, depth=RIGHT_SIDE_DEPTH)

    # build bottom
    bottom_box = primitives.create_box(
        x=RIGHT_SIDE_THICKNESS,
        y=plinth.PLINTH_HEIGHT,
        z=0,
        width=WIDTH - RIGHT_SIDE_THICKNESS,
        height=bottom.BOTTOM_BOARD_THICKNESS,
        depth=bottom.BOTTOM_DEPTH
    )
    builder.add_board_object(Board(bottom_box))

    # build left side
    left_side_box = primitives.create_box(
        x=WIDTH - LEFT_SIDE_THICKNESS,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=LEFT_SIDE_THICKNESS,
        height=LEFT_SIDE_HEIGHT,
        depth=LEFT_SIDE_DEPTH
    )
    builder.add_board_object(Board(left_side_box))

    # build right section
    right_section_box = primitives.create_box(
        x=LEFT_SIDE_THICKNESS + RIGHT_SECTION_WIDTH,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=SECTION_THICKNESS,
        height=LEFT_SIDE_HEIGHT,
        depth=RIGHT_SIDE_DEPTH
    )
    builder.add_board_object(Board(right_section_box))

    # build left section
    left_section_box = primitives.create_box(
        x=LEFT_SIDE_THICKNESS + RIGHT_SECTION_WIDTH + SECTION_THICKNESS + LEFT_SECTION_WIDTH,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=SECTION_THICKNESS,
        height=LEFT_SIDE_HEIGHT,
        depth=RIGHT_SIDE_DEPTH
    )
    builder.add_board_object(Board(left_section_box))

    # build top
    builder.add_board(x=0,
                      y=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
                      z=0,
                      width=WIDTH,
                      height=top.TOP_BOARD_THICKNESS,
                      depth=top.TOP_BOARD_DEPTH)

    # build shelves for left section
    for i in range(4):
        volume = volumes.between(left_side_box, left_section_box, bottom_box, SHELF_HEIGHT, i * SHELF_HEIGHT)
        build_shelf(builder, volume)

    # build shelves for right section
    for i in range(2):
        volume = volumes.between(left_section_box, right_section_box, bottom_box, BIG_SHELF_HEIGHT,
                                 i * BIG_SHELF_HEIGHT)
        build_shelf(builder, volume)
