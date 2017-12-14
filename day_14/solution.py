"""
https://adventofcode.com/2017/day/14
"""
from day10 import get_dense_hash_str
import numpy
import networkx as nx


def from_hex_to_bin(hex_str):
    scale = 16  # equals to hexadecimal
    num_of_bits = 128
    return bin(int(hex_str, scale))[2:].zfill(num_of_bits)


def count_squares(key):
    grid = []
    for i in range(128):
        dense_hash = get_dense_hash_str('-'.join([key, str(i)]))
        binary_str = from_hex_to_bin(dense_hash)
        row_in_binary = []
        for char in binary_str:
            row_in_binary.append(int(char))
        grid.append(row_in_binary)
    grid_arr = numpy.array(grid, dtype=int)
    return grid_arr, grid_arr[grid_arr != 0].sum()


def find_regions(grid):
    graph = nx.generators.lattice.grid_2d_graph(128, 128)
    for x in range(128):
        for y in range(128):
            if not grid[y][x]:
                graph.remove_node((y, x))
    return len(list(nx.connected_components(graph)))


example = 'flqrgnkx'
g, o = count_squares(example)

assert o == 8108
assert find_regions(g) == 1242

if __name__ == '__main__':
    grid, ones = count_squares('nbysizxe')
    print('Part 1:', ones)
    print('Part 2:', find_regions(grid))
