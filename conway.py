#!/usr/bin/env python

"""
An implementation of Conway's Game of Life
using tdl as the graphical library.

TODO:
    * mouse support
    * command line arguments
        * specify grid size
        * example structures
    * render a new window to keep track of current generation
"""

import tdl
from numpy import array, random


# Dimensions of the console
CONSOLE_WIDTH = 60
CONSOLE_HEIGHT = 63

# Dimensions of the world
WORLD_WIDTH = 60
WORLD_HEIGHT = 60

# Dimensions of the panel
PANEL_HEIGHT = 3
PANEL_Y = CONSOLE_HEIGHT - PANEL_HEIGHT

# Colors
COLOR_ON = (0, 0, 0)
COLOR_OFF = (255, 255, 255)

ON = 1
OFF = 0
STATES = [ON, OFF]

# Current generation
GENERATION = 0

def random_grid(width, height):
    """Instantiates a non-uniform random grid of ON/OFF cells."""
    return random.choice(STATES, (width * height), p=[0.2, 0.8]).reshape(width, height)

def render(root, con, panel, cells):
    """Renders the world of cells depending on their state."""
    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if cells[x, y] == 1:
                con.draw_char(x, y, None, bg=COLOR_ON)
            else:
                con.draw_char(x, y, None, bg=COLOR_OFF)

    panel.draw_rect(0,0,None,None,None,bg=(97,117,197))
    panel.draw_str(42,2, 'Generation: ' + str(GENERATION), bg=(97,117,197))
    root.blit(panel,0, PANEL_Y, CONSOLE_WIDTH, PANEL_HEIGHT, 0, 0)
    root.blit(con, 0, 0, WORLD_WIDTH, WORLD_HEIGHT, 0, 0)

def update(cells):
    """Updates the cell state using conway's rules."""
    global GENERATION

    new_cells = cells.copy()

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            # Sums the total of neighbors that are ON
            neighbors = int(cells[(x-1)%WORLD_WIDTH, (y-1)%WORLD_WIDTH] + cells[x, (y-1)%WORLD_WIDTH] + cells[(x+1)%WORLD_WIDTH, (y-1)%WORLD_WIDTH]
                            + cells[(x-1)%WORLD_WIDTH, y] + cells[(x+1)%WORLD_WIDTH, y]
                            + cells[(x-1)%WORLD_WIDTH, (y+1)%WORLD_WIDTH] + cells[x, (y+1)%WORLD_WIDTH] + cells[(x+1)%WORLD_WIDTH, (y+1)%WORLD_WIDTH])

            if cells[x, y] == ON:
                if (neighbors < 2) or (neighbors > 3):
                    new_cells[x, y] = OFF
            else:
                if neighbors == 3:
                    new_cells[x, y] = ON

    cells[:] = new_cells[:]
    GENERATION += 1

def main():
    """The main program loop."""
    root = tdl.init(CONSOLE_WIDTH, CONSOLE_HEIGHT, 'Game-of-Life')
    con = tdl.Console(CONSOLE_WIDTH, CONSOLE_HEIGHT)
    panel = tdl.Console(CONSOLE_WIDTH, PANEL_HEIGHT)
    tdl.set_fps(10)

    cells = random_grid(WORLD_WIDTH, WORLD_HEIGHT)

    while True:
        # TODO: add some program loop control / exit condition
        render(root, con, panel, cells)
        tdl.flush()
        update(cells)

if __name__ == '__main__':
    main()

