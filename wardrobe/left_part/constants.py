import corner_measures
from common import mdf
from wardrobe import top, plinth, bottom, fitting_constants

# this side is slightly bigger that left plasterboard side
WIDTH = corner_measures.LEFT_WALL
"""
Overall width of left wardrobe part
"""

LEFT_SIDE_DEPTH = 0.6
LEFT_SIDE_THICKNESS = mdf.THICK

# this side is slightly "drown" into the wardrobe
RIGHT_SIDE_DEPTH = 0.5

BOTTOM_DEPTH = 0.6

LEFT_SIDE_HEIGHT = corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS
"""
Top board will go on 
"""

RIGHT_SIDE_HEIGHT = corner_measures.HEIGHT \
                    - top.TOP_BOARD_THICKNESS - plinth.PLINTH_HEIGHT - bottom.BOTTOM_BOARD_THICKNESS

RIGHT_SIDE_THICKNESS = mdf.STANDARD

BOTTOM_WIDTH = WIDTH - LEFT_SIDE_THICKNESS

TOP_BOARD_WIDTH = WIDTH

LEFT_COMPARTMENT_WIDTH = 0.3
LEFT_COMPARTMENT_DEPTH = LEFT_SIDE_DEPTH - fitting_constants.RAILS_DEPTH
LEFT_COMPARTMENT_HEIGHT = corner_measures.HEIGHT \
                          - top.TOP_BOARD_THICKNESS - plinth.PLINTH_HEIGHT - bottom.BOTTOM_BOARD_THICKNESS
LEFT_COMPARTMENT_THICKNESS = mdf.STANDARD
