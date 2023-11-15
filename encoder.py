### This file contains the logic for converting a world or a list of world frames into an animation or image ###

import numpy as np
from PIL import Image
from tile import TileType, TILE_COLORS

def save_frames(frames, file_name):
    """
    Saves a sequence of frames (images) as an animation (GIF or video).

    :param frames: A list or sequence of frames (images).
    :param file_name: The name of the file to save the animation.
    """
    # TODO
    pass

def world_to_image(world):
    """
    Converts the world grid to an image.

    :param world: The world grid.
    :return: A PIL image representing the world.
    """
    height, width = world.shape
    image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            tile_value = world[x, y]
            color = TILE_COLORS.get(tile_value, (255, 0, 255))  # Default to magenta if not found
            image.putpixel((x, y), color)

    return image
