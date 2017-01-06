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


WIDTH = 60
HEIGHT = 60

COLOR_ON = (0, 0, 0)
COLOR_OFF = (255, 255, 255)

ON = 1
OFF = 0

STATES = [ON, OFF]

def random_grid(height, width):
    """Instantiates a non-uniform random grid of ON/OFF cells."""
    return random.choice(STATES, (height * width), p=[0.2, 0.8]).reshape(height, width)

def render(root, con, cells):
    """Renders the world of cells depending on their state."""
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if cells[x, y] == 1:
                con.draw_char(x, y, None, bg=COLOR_ON)
            else:
                con.draw_char(x, y, None, bg=COLOR_OFF)

    root.blit(con, 0, 0, WIDTH, HEIGHT, 0, 0)

def update(cells):
    """Updates the cell state using conway's rules."""
    new_cells = cells.copy()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Sums the total of neighbors that are ON
            neighbors = int(cells[(x-1)%WIDTH, (y-1)%WIDTH] + cells[x, (y-1)%WIDTH] + cells[(x+1)%WIDTH, (y-1)%WIDTH]
                            + cells[(x-1)%WIDTH, y] + cells[(x+1)%WIDTH, y]
                            + cells[(x-1)%WIDTH, (y+1)%WIDTH] + cells[x, (y+1)%WIDTH] + cells[(x+1)%WIDTH, (y+1)%WIDTH])

            if cells[x,y] == ON:
                if (neighbors < 2) or (neighbors > 3):
                    new_cells[x, y] = OFF
            else:
                if neighbors == 3:
                    new_cells[x, y] = ON

    cells[:] = new_cells[:]

def main():
    """The main program loop."""
    root = tdl.init(HEIGHT, WIDTH, 'Game-of-Life')
    con = tdl.Console(HEIGHT, WIDTH)
    tdl.set_fps(10)

    cells = random_grid(HEIGHT, WIDTH)

    while True:
        # TODO: add some program loop control / exit condition
        render(root, con, cells)
        tdl.flush()
        update(cells)

if __name__ == '__main__':
    main()

