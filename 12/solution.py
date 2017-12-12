"""
https://adventofcode.com/2017/day/12
"""

import re
import networkx as nx


class Node:
    """
    Class to build a node id and it's connections from the provided string
    representation.
    """

    def __init__(self, string_representation):
        self.regexp = re.compile(r'(?P<id>\d+) <-> (?P<connections>.*)')
        self.string_representation = string_representation
        self.match_string()

    def match_string(self):
        match = self.regexp.match(self.string_representation)
        self.id = int(match.groupdict()['id'])
        self.connections = list(map(int, match.groupdict()['connections'].split(',')))


def build_network(puzzle):
    if type(puzzle) == str:
        puzzle = puzzle.split('\n')
    list_of_nodes = [Node(n) for n in puzzle]
    network = {
        n.id: n.connections for n in list_of_nodes
    }
    return network


def count_members_root_subgroup(network, root):
    G = nx.Graph(network)
    for subgraph in nx.connected_component_subgraphs(G):
        if root in subgraph.nodes:
            return subgraph.number_of_nodes()


def total_number_of_groups(network):
    G = nx.Graph(network)
    count = 0
    for _ in nx.connected_component_subgraphs(G):
        count += 1
    return count

example = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

assert count_members_root_subgroup(
    network=build_network(example),
    root=0
) == 6

assert total_number_of_groups(build_network(example)) == 2

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.readlines()

    puzzle_nt = build_network(puzzle)
    print('Part 1:', count_members_root_subgroup(puzzle_nt, 0))
    print('Part 2:', total_number_of_groups(puzzle_nt))
