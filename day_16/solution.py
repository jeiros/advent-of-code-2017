"""
https://adventofcode.com/2017/day/16
"""


def spin(string, amount):
    new_string = [letter for letter in string]
    for i in range(len(string)):
        new_i = (i + amount) % len(string)
        new_string[new_i] = string[i]
    return ''.join(new_string)


def exchange(string, pos1, pos2):
    new_string = [letter for letter in string]
    new_string[pos1] = string[pos2]
    new_string[pos2] = string[pos1]
    return ''.join(new_string)


def partner(string, programA, programB):
    iA = string.index(programA)
    iB = string.index(programB)
    return exchange(string, iA, iB)


def parse_instruction(instruction, string):
    if 's' in instruction:
        amount = int(instruction[1:])
        return spin(string, amount)
    elif 'x' in instruction:
        inst_split = instruction.split('/')
        p1 = int(inst_split[0][1:])
        p2 = int(inst_split[1])
        return exchange(string, p1, p2)
    else:
        inst_split = instruction.split('/')
        pA = inst_split[0][1:]
        pB = inst_split[1]
        return partner(string, pA, pB)


assert spin('abcde', 1) == 'eabcd'
assert exchange('eabcd', 3, 4) == 'eabdc'
assert partner('eabdc', 'e', 'b') == 'baedc'


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        instructions_list = f.readline().strip('\n').split(',')
    # Part 1
    puzzle = 'abcdefghijklmnop'
    for inst in instructions_list:
        puzzle = parse_instruction(inst, puzzle)
    print('Part 1:', puzzle)
    # Part 2
    puzzle = 'abcdefghijklmnop'
    seen_strings = [puzzle]
    i = 0
    a_billion = 1000000000
    for _ in range(a_billion):
        for inst in instructions_list:
            puzzle = parse_instruction(inst, puzzle)
        i += 1
        if puzzle in seen_strings:
            break
        else:
            seen_strings.append(puzzle)
    print('Part 2:', seen_strings[a_billion % i])
