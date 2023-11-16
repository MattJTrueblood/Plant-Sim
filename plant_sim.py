### This file contains the main logic for running the simulation itself ###

import numpy as np
import random
from tile import TileType

MIN_SOIL_DEPTH = 5 # the shallowest possible depth for soil in the simulation
MAX_SOIL_DEPTH = 15 # The highest possible depth for soil in the simulation
TERRAIN_FLATNESS = 0.5 # A parameter which controls how flat the terrain is. 1.0=perfectly flat; 0.0=never flat


def create_world(width, height):
    """
    Creates the initial grid for the simulation.

    :param width: Width of the world.
    :param height: Height of the world.
    :return: The created world (grid).
    """
    world = np.zeros(shape=(width, height)) # all tiles are by default empty
    
    add_soil_random_walk(world)
    add_seeds(world, 3)
    
    return world


def add_soil_random_walk(world):
    """
    Populates the world with a random terrain of soil tiles generated using a random walk method.
    The random walk is controlled by a min and max elevation, as well as a flatness parameter which weights the random walk.
    
    :param world: the world to add the soil to
    """
    soil_depth = random.randint(MIN_SOIL_DEPTH, MAX_SOIL_DEPTH)
    width, height = world.shape

    for i in range(width):
        # Calculate the top boundary of the soil based on the soil depth and fill in all tiles below it.
        soil_top = height - soil_depth
        world[i, soil_top:] = TileType.SOIL.value

        # Randomly choose to either move soil_depth up 1, down 1, or stay the same, based on flatness.
        if soil_depth > MIN_SOIL_DEPTH and soil_depth < MAX_SOIL_DEPTH:
            change = random.choices([-1, 0, 1], weights=[1 - TERRAIN_FLATNESS, TERRAIN_FLATNESS, 1 - TERRAIN_FLATNESS])[0]
        elif soil_depth <= MIN_SOIL_DEPTH:
            change = random.choices([0, 1], weights=[TERRAIN_FLATNESS, 1 - TERRAIN_FLATNESS])[0]
        else:  # soil_depth >= MAX_SOIL_DEPTH
            change = random.choices([-1, 0], weights=[1 - TERRAIN_FLATNESS, TERRAIN_FLATNESS])[0]
            
        soil_depth += change
        
def add_seeds(world, num_seeds):
    """
    Places a given quantity of plant seeds in the soil.
    
    :param world: the world to add the seeds to
    :param num_seeds: the number of seeds to add to the world
    """
    width, height = world.shape
    for _ in range(num_seeds):
        seed_x = random.randint(0, width)
        # Find the y value of the topmost soil tile in this column and place the seed there
        for seed_y in range(height):
            if world[seed_x, seed_y] == TileType.SOIL.value:
                world[seed_x, seed_y] = TileType.SEED.value
                break;
    

def run_sim(world, num_steps):
    """
    Runs the simulation for a given number of steps.

    :param world: The world (grid) on which to run the simulation.
    :param num_steps: Number of steps to run the simulation.
    :return: A numpy array of frames for each step of the simulation
    """
    # TODO
    pass
