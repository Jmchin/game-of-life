#!/usr/bin/env python

import tdl
from numpy import array, random

"""
An implementation of Conway's Game of Life
using tdl as the graphical library.

TODO:
    setup the World - a 1D-list of cells
    setup the cells - need to be aware of neighbors
    handle edge conditions
        * toroidal geometry
        * or do not allow edges to be populated
"""

WIDTH = 100
HEIGHT = 100

COLOR_ON = (0, 0, 0)
COLOR_OFF = (255, 255, 255)

ON = 1
OFF = 0

STATES = [ON, OFF]

def random_grid(height, width):
    """instantiates a non-uniform random grid of ON/OFF cells"""
    return random.choice(STATES, (height * width), p=[0.2, 0.8]).reshape(height, width)

def render(root, con, cells):
    """renders the world of cells depending on their state"""
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cell = cells[x][y]
            if cell == 1:
                con.draw_char(x, y, None, bg=COLOR_ON)
            else:
                con.draw_char(x, y, None, bg=COLOR_OFF)

    root.blit(con, 0, 0, WIDTH, HEIGHT, 0, 0)

def update(cells):
    """updates the cell state using conway's rules"""
    new_cells = cells.copy()

    for x in range(WIDTH-1):
        for y in range(HEIGHT-1):
            #neighbors = int(cells[x, (y-1)%WIDTH] + cells[x, (y+1)%WIDTH] +
            #                 cells[(x-1)%WIDTH, y] + cells[(x+1)%WIDTH, y] +
            #                 cells[(x+1)%WIDTH, (y-1)%WIDTH] + cells[(x+1)%WIDTH, (y+1)%WIDTH])

            neighbors = int(cells[(x-1)%WIDTH, (y-1)%WIDTH] + cells[x, (y-1)%WIDTH] + cells[(x+1)%WIDTH, (y-1)%WIDTH] +
                           cells[(x-1)%WIDTH, y] + cells[(x+1)%WIDTH, y] +
                           cells[(x-1)%WIDTH, (y+1)%WIDTH] + cells[x, (y+1)%WIDTH] + cells[(x+1)%WIDTH, (y+1)%WIDTH])

            if cells[x,y] == ON:
                if (neighbors < 2) or (neighbors > 3):
                    new_cells[x,y] = OFF
            else:
                if neighbors == 3:
                    new_cells[x,y] = ON

    #import pdb; pdb.set_trace()
    cells[:] = new_cells[:]

def main():
    """main program loop"""
    root = tdl.init(HEIGHT, WIDTH, 'Game-of-Life')
    con = tdl.Console(HEIGHT, WIDTH)
    tdl.set_fps(10)

    cells = random_grid(HEIGHT, WIDTH)

    while True:
        render(root, con, cells)
        tdl.flush()
        update(cells)
        #import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()

