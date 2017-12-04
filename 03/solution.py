"""
http://adventofcode.com/2017/day/3
"""
import numpy
from itertools import cycle


def distance_to_center(coordinates):
    return sum(map(abs, coordinates))


def find_end(layer):
    return (4 * layer ** 2) + (4 * layer) + 1


def find_layer(number):
    layer = 1
    end_layer = find_end(layer)
    while number > end_layer:
        layer += 1
        end_layer = find_end(layer)
    return layer


def find_position(number):
    if number == 1:
        return (0, 0)
    layer = find_layer(number)
    end_of_layer_no = find_end(layer)
    sides_of_layer = 2 * layer

    corners_of_layer = [end_of_layer_no - sides_of_layer * i
                        for i in range(0, 4)]

    corner_coords = [
        (layer, layer),  # top right (smallest number)
        (-layer, layer),  # top left
        (-layer, -layer),  # bottom left
        (layer, -layer),  # bottom right (end_of_layer_no)

    ]

    side = 0
    for c in sorted(corners_of_layer):
        if number <= c:
            num_dist = abs(c - number)
            c_coords = corner_coords[side]
            break
        side += 1

    if side == 0:
        # right side
        number_position = (
            c_coords[0],
            c_coords[1] - num_dist
        )
    elif side == 1:
        # top side
        number_position = (
            c_coords[0] + num_dist,
            c_coords[1]
        )
    elif side == 2:
        # left side
        number_position = (
            c_coords[0],
            c_coords[1] + num_dist
        )
    elif side == 3:
        # bottom side
        number_position = (
            c_coords[0] - num_dist,
            c_coords[1]
        )

    return number_position

# part 2, dirty way, build spiral in a big np array


def neighbours(arr, coord):
    x, y = coord
    return arr[x - 1: x + 2, y - 1: y + 2]


def part2(puzzle):
    directions = [
        (0, 1),  # right
        (-1, 0),  # up
        (0, -1),  # left
        (1, 0)  # down
    ]
    spiral = [[0] * 41 for x in range(41)]
    spiral[20][20] = 1
    spiral = numpy.asarray(spiral)
    current_pos = (20, 20)
    written_no = 1

    rep = 1
    move_counter = 0
    licycle = cycle(directions)
    for move in licycle:
        for i in range(rep):
            x, y = move[0], move[1]
            new_x, new_y = current_pos[0] + x, current_pos[1] + y
            new_coords = new_x, new_y
            written_no = neighbours(spiral, new_coords).sum()
            if written_no > puzzle:
                return written_no
            spiral[new_x][new_y] = written_no
            current_pos = new_coords

        move_counter += 1
        if move_counter == 2:
            move_counter = 0
            rep += 1


if __name__ == '__main__':
    puzzle = 277678
    assert distance_to_center(find_position(1)) == 0
    assert distance_to_center(find_position(12)) == 3
    assert distance_to_center(find_position(23)) == 2
    assert distance_to_center(find_position(1024)) == 31

    print('Part 1: ', distance_to_center(find_position(puzzle)))
    print('Part 2: ', part2(puzzle))
