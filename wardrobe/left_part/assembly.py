import corner_measures
# TODO fix this strange import
import wardrobe.left_part.constants as left_part_constants
from builder.wardrobe_builder import WardrobeBuilder
from wardrobe import plinth, bottom, top


def build(builder: WardrobeBuilder):
    """
    Build the left part of the wardrobe

    Build everything within left wall context.
    """

    # build starting from the left wall with X axis pointing to the origin
    builder.set_origin(x0=corner_measures.LEFT_WALL, y0=0, z0=0, x1=-1, y1=1, z1=1)
    builder.use_iXYZ()

    # build left side
    builder.add_board(x=0,
                      y=0,
                      z=0,
                      width=left_part_constants.LEFT_SIDE_THICKNESS,
                      height=corner_measures.HEIGHT,
                      depth=left_part_constants.LEFT_SIDE_DEPTH)

    # build bottom
    builder.add_board(x=left_part_constants.LEFT_SIDE_THICKNESS,
                      y=plinth.PLINTH_HEIGHT,
                      z=0,
                      width=left_part_constants.BOTTOM_WIDTH,
                      height=bottom.BOTTOM_BOARD_THICKNESS,
                      depth=bottom.BOTTOM_DEPTH)

    # put right side on the bottom
    builder.add_board(
        x=left_part_constants.LEFT_SIDE_THICKNESS + left_part_constants.BOTTOM_WIDTH - left_part_constants.RIGHT_SIDE_THICKNESS,
        y=plinth.PLINTH_HEIGHT + bottom.BOTTOM_BOARD_THICKNESS,
        z=0,
        width=left_part_constants.RIGHT_SIDE_THICKNESS,
        height=left_part_constants.RIGHT_SIDE_HEIGHT,
        depth=left_part_constants.RIGHT_SIDE_DEPTH)

    # build top
    builder.add_board(x=0,
                      y=corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS,
                      z=0,
                      width=left_part_constants.TOP_BOARD_WIDTH,
                      height=top.TOP_BOARD_THICKNESS,
                      depth=top.TOP_BOARD_DEPTH)
