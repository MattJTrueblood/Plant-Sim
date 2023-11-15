### This file contains shared tile constants and types used in multiple places in the project ###

from enum import Enum

# TileType is an enum for how to store the tile types as simple integer values
class TileType(Enum):
    EMPTY = 0
    SOIL = 1
    PLANT = 2
    SEED = 3
    
# TILE_COLORS is a mapping from tile types to their display colors.
TILE_COLORS = {
    TileType.EMPTY.value: (255, 255, 255),
    TileType.SOIL.value: (139, 69, 19),
    TileType.PLANT.value: (34, 139, 34),
    TileType.SEED.value: (0, 0, 0),
}