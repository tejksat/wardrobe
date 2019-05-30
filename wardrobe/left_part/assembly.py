import corner_measures
# TODO fix this strange import
import wardrobe.left_part.constants as left_part_constants
import wardrobe.right_part.constants as right_part_constants
from builder import volumes, primitives
from builder.boards import Board
from builder.primitives import Box, Point
from builder.wardrobe_builder import WardrobeBuilder
from wardrobe import plinth, bottom, top
from wardrobe.top_shelf import TOP_SHELF_THICKNESS, TOP_SHELF_HEIGHT_FROM_FLOOR


def build(builder: WardrobeBuilder):
    """
    Build the left part of the wardrobe

    Build everything within left wall context.
    """

    # build starting from the left wall with X axis pointing to the origin
    builder.set_origin(x0=corner_measures.LEFT_WALL, y0=0, z0=0, x1=-1, y1=1, z1=1)
    builder.use_iXYZ()

    # build left side
    left_side_box = primitives.create_box(
        x=0,
        y=0,
        z=0,
        width=left_part_constants.LEFT_SIDE_THICKNESS,
        height=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
        depth=left_part_constants.LEFT_SIDE_DEPTH
    )
    builder.add_board_object(Board(left_side_box))

    # build right side
    right_side_box = primitives.create_box(
        x=corner_measures.LEFT_WALL - left_part_constants.RIGHT_SIDE_THICKNESS,
        y=0,
        z=0,
        width=left_part_constants.RIGHT_SIDE_THICKNESS,
        height=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
        depth=left_part_constants.RIGHT_SIDE_DEPTH
    )
    builder.add_board_object(Board(right_side_box))

    # build bottom
    builder.add_board(x=left_part_constants.LEFT_SIDE_THICKNESS,
                      y=plinth.PLINTH_HEIGHT,
                      z=0,
                      width=left_part_constants.BOTTOM_WIDTH,
                      height=bottom.BOTTOM_BOARD_THICKNESS,
                      depth=bottom.BOTTOM_DEPTH)

    # build section divider board on the bottom
    section_divider_box = primitives.create_box(
        x=left_part_constants.LEFT_SIDE_THICKNESS + left_part_constants.LEFT_COMPARTMENT_WIDTH,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=left_part_constants.LEFT_COMPARTMENT_THICKNESS,
        height=left_part_constants.LEFT_COMPARTMENT_HEIGHT,
        depth=left_part_constants.LEFT_COMPARTMENT_DEPTH
    )
    builder.add_board_object(Board(section_divider_box))

    # build top
    builder.add_board(x=0,
                      y=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
                      z=0,
                      width=left_part_constants.TOP_BOARD_WIDTH,
                      height=top.TOP_BOARD_THICKNESS,
                      depth=top.TOP_BOARD_DEPTH)

    # build top shelves
    volume = volumes.between_two(left_side_box, section_divider_box, TOP_SHELF_THICKNESS, TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    volume = volumes.between_two(section_divider_box, right_side_box, TOP_SHELF_THICKNESS, TOP_SHELF_HEIGHT_FROM_FLOOR)
    builder.add_board_object(Board(volume))

    # add plinth
    plinth_box = Box(
        Point(
            left_part_constants.LEFT_SIDE_THICKNESS,
            0,
            left_part_constants.LEFT_SIDE_DEPTH - (plinth.PLINTH_OFFSET - plinth.PLINTH_THICKNESS)
        ),
        Point(
            corner_measures.LEFT_WALL - (right_part_constants.RIGHT_SIDE_DEPTH - plinth.PLINTH_OFFSET),
            plinth.PLINTH_HEIGHT,
            left_part_constants.LEFT_SIDE_DEPTH - plinth.PLINTH_OFFSET
        )
    )
    builder.add_board_object(Board(plinth_box))
