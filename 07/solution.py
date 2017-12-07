"""
https://adventofcode.com/2017/day/7
"""


def find_bottom(puzzle):
    list_of_programs = []
    subprograms = []
    for line in puzzle:
        program_name = line.split()[0]
        if len(line.split('->')) == 2:
            for subprgr in line.split('->')[-1].split(','):
                subprograms.append(subprgr.strip())
        list_of_programs.append(program_name)

    for program in list_of_programs:
        if program not in subprograms:
            return program


example = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

ex_list = example.split('\n')

assert find_bottom(ex_list) == 'tknk'


def get_own_weight(program_name, puzzle):
    for line in puzzle:
        if program_name == line.split()[0]:
            own_weight = int(line.split(' ')[1].strip('()'))
    return own_weight


def get_all_weights(program_name, puzzle):
    total_weight = get_own_weight(program_name, puzzle)
    for line in puzzle:
        if program_name == line.split()[0]:
            split_arrow = line.split('->')
            if len(split_arrow) == 2:
                discs = split_arrow[1].split(',')
                discs_list = [x.strip() for x in discs]
                for d in discs_list:
                    total_weight += get_all_weights(d, puzzle)
                return total_weight
            else:
                return get_own_weight(program_name, puzzle)


def find_unbalanced(bottom, puzzle):
    weights = {}
    for line in puzzle:
        if bottom == line.split()[0]:
            split_arrow = line.split('->')
            discs = split_arrow[1].split(',')
            discs_list = [x.strip() for x in discs]

            for d in discs_list:
                own_w = get_own_weight(d, puzzle)
                weights[(d, own_w)] = get_all_weights(d, puzzle)

    if len(set(weights.values())) == 1:
        # All balanced
        return None
    else:
        for k, v in weights.items():
            if list(weights.values()).count(v) == 1:
                unbalanced_node = k[0]
                original_w = k[1]
                total_w = v
        for k, v in weights.items():
            if v != total_w:
                diff = v - total_w
                break
            else:
                diff = 0

        new_weight = original_w + diff

        return new_weight, find_unbalanced(unbalanced_node, puzzle)


assert find_unbalanced('tknk', ex_list)[0] == 60

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.readlines()
    print('Part 1:', find_bottom(puzzle))
    print('Part 2:', find_unbalanced(find_bottom(puzzle),
                                     [i.strip('\n') for i in puzzle]))
