import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
min_x = 0
min_y = 0
max_x = w
max_y = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    #print("Debug messages...", file=sys.stderr, flush=True)

    if bomb_dir in ['D', 'DR', 'DL']:

        min_y = y0
        y0 = (y0 + max_y) // 2

    if bomb_dir in ['U', 'UR', 'UL']:

        max_y = y0
        y0 = (y0 + min_y) // 2

    if bomb_dir in ['R', 'UR', 'DR']:

        min_x = x0
        x0 = (x0 + max_x) // 2

    if bomb_dir in ['L', 'UL', 'DL']:

        max_x = x0
        x0 = (x0 + min_x) // 2

    # the location of the next window Batman should jump to.
    print(x0, y0)