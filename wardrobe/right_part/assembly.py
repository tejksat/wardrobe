import corner_measures
import wardrobe.left_part.constants as left_part_constants
from builder import volumes, primitives
from builder.boards import Board
from builder.primitives import Box, Point
from builder.shelves import build_shelf
from builder.wardrobe_builder import WardrobeBuilder
from common import mdf
from wardrobe import plinth, bottom, top
from wardrobe.right_part.constants import LEFT_SIDE_DEPTH, LEFT_SECTION_WIDTH, OPEN_SECTION_WIDTH
from wardrobe.top_shelf import TOP_SHELF_THICKNESS, TOP_SHELF_HEIGHT_FROM_FLOOR
from .constants import (
    WIDTH,
    RIGHT_SIDE_DEPTH,
    RIGHT_SIDE_HEIGHT,
    RIGHT_SIDE_THICKNESS,
    LEFT_SIDE_THICKNESS,
    LEFT_SIDE_HEIGHT,
    SECTION_THICKNESS,
    RIGHT_SECTION_WIDTH,
    MIDDLE_SECTION_WIDTH
)

# todo move to constants
SHELF_HEIGHT = 0.2
BIG_SHELF_HEIGHT = 0.4


def build(builder: WardrobeBuilder):
    # build starting from the right wall with Y axis pointing to the origin
    builder.set_origin(x0=0, y0=0, z0=corner_measures.RIGHT_WALL, x1=1, y1=1, z1=-1)
    builder.use_ZYiX()

    # build right side
    right_side_box = primitives.create_box(
        x=0,
        y=0,
        z=0,
        width=RIGHT_SIDE_THICKNESS,
        height=RIGHT_SIDE_HEIGHT,
        depth=RIGHT_SIDE_DEPTH
    )
    builder.add_board_object(Board(right_side_box))

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

    # build left side of shelves compartment
    shelves_compartment_box = primitives.create_box(
        x=WIDTH - LEFT_SIDE_THICKNESS,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=LEFT_SIDE_THICKNESS,
        height=SHELF_HEIGHT * 4,
        depth=LEFT_SIDE_DEPTH
    )
    builder.add_board_object(Board(shelves_compartment_box))

    # build left section
    left_section_box = primitives.create_box(
        x=RIGHT_SECTION_WIDTH + MIDDLE_SECTION_WIDTH + LEFT_SECTION_WIDTH,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=LEFT_SIDE_THICKNESS,
        height=LEFT_SIDE_HEIGHT,
        depth=LEFT_SIDE_DEPTH
    )
    builder.add_board_object(Board(left_section_box))

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

    # build middle section
    middle_section_box = primitives.create_box(
        x=LEFT_SIDE_THICKNESS + RIGHT_SECTION_WIDTH + SECTION_THICKNESS + MIDDLE_SECTION_WIDTH,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=SECTION_THICKNESS,
        height=LEFT_SIDE_HEIGHT,
        depth=RIGHT_SIDE_DEPTH
    )
    builder.add_board_object(Board(middle_section_box))

    # build top
    builder.add_board(x=0,
                      y=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
                      z=0,
                      width=WIDTH,
                      height=top.TOP_BOARD_THICKNESS,
                      depth=top.TOP_BOARD_DEPTH)

    # build shelves for left section
    for i in range(4):
        volume = volumes.between(left_section_box, middle_section_box, bottom_box, SHELF_HEIGHT, i * SHELF_HEIGHT)
        build_shelf(builder, volume)

    volume = volumes.between(left_section_box, middle_section_box, bottom_box, mdf.STANDARD, 4 * SHELF_HEIGHT)
    builder.add_board_object(Board(volume))

    # build shelves for right section
    for i in range(2):
        volume = volumes.between(middle_section_box, right_section_box, bottom_box, BIG_SHELF_HEIGHT,
                                 i * BIG_SHELF_HEIGHT)
        build_shelf(builder, volume)

    volume = volumes.between(middle_section_box, right_section_box, bottom_box, mdf.STANDARD, 4 * SHELF_HEIGHT)
    builder.add_board_object(Board(volume))

    # build shelves for the compartment
    for i in range(4):
        volume = volumes.between(shelves_compartment_box, left_section_box, bottom_box, SHELF_HEIGHT, i * SHELF_HEIGHT)
        build_shelf(builder, volume)

    # build top shelves
    volume = volumes.between_two(left_section_box, middle_section_box, TOP_SHELF_THICKNESS,
                                 TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    volume = volumes.between_two(middle_section_box, right_section_box, TOP_SHELF_THICKNESS,
                                 TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    volume = volumes.between_two(right_section_box, right_side_box, TOP_SHELF_THICKNESS,
                                 TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    volume = volumes.right_from(left_section_box, OPEN_SECTION_WIDTH, TOP_SHELF_THICKNESS, TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    # add plinth
    plinth_box = Box(
        Point(
            RIGHT_SIDE_THICKNESS,
            0,
            RIGHT_SIDE_DEPTH - (plinth.PLINTH_OFFSET - plinth.PLINTH_THICKNESS)
        ),
        Point(
            corner_measures.RIGHT_WALL - (left_part_constants.LEFT_SIDE_DEPTH - plinth.PLINTH_OFFSET),
            plinth.PLINTH_HEIGHT,
            RIGHT_SIDE_DEPTH - plinth.PLINTH_OFFSET
        )
    )
    builder.add_board_object(Board(plinth_box))
