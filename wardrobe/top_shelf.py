import corner_measures
from common import mdf
from wardrobe import top

TOP_SHELF_THICKNESS = mdf.STANDARD
TOP_SHELF_HEIGHT = 0.3
TOP_SHELF_HEIGHT_FROM_FLOOR = corner_measures.HEIGHT - top.TOP_BOARD_THICKNESS - TOP_SHELF_HEIGHT - TOP_SHELF_THICKNESS
