"""
https://adventofcode.com/2017/day/11
"""


def get_coords(steps):
    furthest = 0
    backward_paths = {
        'n': (0, -1),
        'ne': (1, -1),
        'se': (1, 0),
        's': (0, 1),
        'sw': (-1, 1),
        'nw': (-1, 0)
    }
    coords = (0, 0)
    if type(steps) == str:
        steps = steps.split(',')
    for step in steps:
        coords = (
            coords[0] + backward_paths[step][0],
            coords[1] + backward_paths[step][1],
        )
        curr_dist = distance_to_center(coords)
        furthest = max(furthest, curr_dist)
    return coords, furthest


def hex_distance(a, b):
    return (abs(a[0] - b[0])
            + abs(a[0] + a[1] - b[0] - b[1])
            + abs(a[1] - b[1])) / 2


def distance_to_center(coords):
    return hex_distance(coords, (0, 0))


assert distance_to_center(get_coords('ne,ne,ne')[0]) == 3
assert distance_to_center(get_coords('ne,ne,sw,sw')[0]) == 0
assert distance_to_center(get_coords('ne,ne,s,s')[0]) == 2
assert distance_to_center(get_coords('se,sw,se,sw,sw')[0]) == 3


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.readline()

    final_coords, furthest = get_coords(puzzle.strip('\n'))
    print('Part 1:', distance_to_center(final_coords))
    print('Part 2:', furthest)
