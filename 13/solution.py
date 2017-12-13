"""
https://adventofcode.com/2017/day/13
"""
from itertools import cycle
from copy import deepcopy


class Layer:

    def __init__(self, layer, depth):
        self.layer = layer
        if type(self.layer) == list:
            max_ind = len(layer)
            self.range = max_ind
            self.depth = depth
            self.position_iterator = cycle(
                list(range(0, max_ind)) +
                list(reversed(list(range(0, max_ind))[1:-1]))
            )
            next(self.position_iterator)

    def __len__(self):
        return len(self.layer)

    def update_layer(self):
        copy_layer = [i for i in self.layer]
        if self.layer == '...':
            copy_layer = '...'
        else:
            index_S = copy_layer.index('S')
            new_index_S = next(self.position_iterator)
            copy_layer[index_S] = None
            copy_layer[new_index_S] = 'S'
        self.layer = copy_layer


class Firewall:

    def __init__(self, structure):
        self.structure = structure
        self.init_state = self.parse_structure()
        self.state = [layer for layer in self.init_state]
        self.picosecond = 0
        self.packet_position = 0
        self.severity = 0
        self.caught = False

    def __repr__(self):
        doc = 'Picosecond {ps}:\n'.format(ps=self.picosecond)
        for i in range(len(self.state)):
            doc += ' {id} \t'.format(id=i)
        doc += '\n'
        max_depth = 0
        for layer in self.state:
            max_depth = max(max_depth, len(layer))
        for i in range(max_depth):
            for j in range(len(self.state)):
                if self.state[j].layer == '...':
                    if i == 0:
                        if self.packet_position == j:
                            doc += '(.)\t'
                        else:
                            doc += '...\t'
                    else:
                        doc += '   \t'
                elif type(self.state[j].layer == list):
                    try:
                        if self.state[j].layer[i] is None:
                            doc += '[ ]\t'
                        else:
                            doc += '[' + self.state[j].layer[i] + ']\t'
                    except:
                        doc += '   \t'
            doc += '\n'
        return doc

    def parse_structure(self):
        layers_ranges = {}
        for line in self.structure.split('\n'):
            split_line = line.split(':')
            layer_no = int(split_line[0])
            depth = int(split_line[1])
            layers_ranges[layer_no] = depth
        return self.build_init_state(layers_ranges)

    def build_init_state(self, layers_ranges):
        structure = []
        for i in range(0, max(layers_ranges.keys()) + 1):
            if i in layers_ranges.keys():
                layer = [
                    None for _ in range(layers_ranges[i])
                ]
                layer[0] = 'S'
            else:
                layer = '...'
            layer_obj = Layer(layer, i)
            structure.append(layer_obj)
        return structure

    def update_scanners(self):
        current_state_copy = [layer for layer in self.state]
        for layer in current_state_copy:
            layer.update_layer()
        self.state = current_state_copy
        self.picosecond += 1

    def update_packet_position(self):
        self.packet_position += 1
        if self.state[self.packet_position].layer[0] == 'S':
            self.severity += (
                self.state[self.packet_position].depth *
                self.state[self.packet_position].range
            )
            self.caught = True


def find_severity(firewall):
    while firewall.packet_position < len(firewall.state) - 1:
        firewall.update_scanners()
        firewall.update_packet_position()
    return firewall.severity


def find_delay(puzzle):
    delay = 0
    finished = False
    firewall = Firewall(puzzle)
    while not finished:
        copy_firewall = deepcopy(firewall)
        while firewall.packet_position < len(firewall.state) - 1:
            if firewall.packet_position == 0 and firewall.state[0].layer[0] == 'S':
                firewall.caught = True
            firewall.update_scanners()
            firewall.update_packet_position()

        if firewall.caught:
            delay += 1
            copy_firewall.update_scanners()
            firewall = deepcopy(copy_firewall)
            firewall.packet_position = 0
            firewall.caught = False
        else:
            print('Finished at delay ', delay)
            finished = True

        if delay % 5000 == 0:
            print(delay)
    return delay

example = """0: 3
1: 2
4: 4
6: 4"""

assert find_severity(Firewall(example)) == 24


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = file.read()

    print('Part 1:', find_severity(Firewall(puzzle)))
    find_delay(puzzle)
