import corner_measures
from common import mdf
from wardrobe import top, plinth, bottom
from ..left_part import constants as left_part_constants

WIDTH = corner_measures.RIGHT_WALL - left_part_constants.LEFT_SIDE_DEPTH

RIGHT_SIDE_DEPTH = 0.6
RIGHT_SIDE_THICKNESS = mdf.THICK
RIGHT_SIDE_HEIGHT = corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS

LEFT_SIDE_THICKNESS = mdf.STANDARD
LEFT_SIDE_HEIGHT = corner_measures.HEIGHT \
                   - top.TOP_BOARD_THICKNESS - plinth.PLINTH_HEIGHT - bottom.BOTTOM_BOARD_THICKNESS

# for WingLine L
# 30.5 mm from the corner to the center + half of rail width
RAILS_DEPTH = 0.04

LEFT_SIDE_DEPTH = RIGHT_SIDE_DEPTH - RAILS_DEPTH

LEFT_SECTION_WIDTH = 0.5
MIDDLE_SECTION_WIDTH = 0.5
RIGHT_SECTION_WIDTH = 0.3
OPEN_SECTION_WIDTH = corner_measures.RIGHT_WALL - left_part_constants.LEFT_COMPARTMENT_DEPTH
"""
Width of the leftmost section (that is connected with left wardrobe part).
"""

SECTION_THICKNESS = mdf.STANDARD
