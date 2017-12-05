"""
https://adventofcode.com/2017/day/5
"""


def escape(moves):
    moves_touch = [i for i in moves]
    pointer = 0
    it = 0
    while pointer < len(moves_touch):
        p = moves_touch[pointer]
        moves_touch[pointer] += 1
        pointer += p
        it += 1
    return it


def escape_2(moves):
    moves_touch = [i for i in moves]
    pointer = 0
    it = 0
    while pointer < len(moves_touch):
        p = moves_touch[pointer]
        if p >= 3:
            moves_touch[pointer] -= 1
        else:
            moves_touch[pointer] += 1
        pointer += p
        it += 1
    return it

test_moves = [
    0,
    3,
    0,
    1,
    -3
]
assert escape(test_moves) == 5
assert escape_2(test_moves) == 10

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = list(map(int, f.readlines()))

    print('Part 1:', escape(puzzle))
    print('Part 2:', escape_2(puzzle))
