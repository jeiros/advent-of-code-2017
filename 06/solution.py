"""
https://adventofcode.com/2017/day/6
"""


def choose_index_bank(banks):
    """
    Finds the memory bank with the most blocks
    (ties won by the lowest-numbered memory bank)

    Parameters
    ----------
    banks: list of ints

    Returns
    -------
    index: int, Index of the chose memory bank
    """
    max_value = max(banks)
    return banks.index(max_value)


def distribute_blocks(banks):
    """
    Redistributes blocks among the banks.
    To do this, it removes all of the blocks from
    the selected bank, then moves to the next (by index)
    memory bank and inserts one of the blocks.
    It continues doing this until it runs out of blocks;
    if it reaches the last memory bank,
    it wraps around to the first one.
    """
    copy_banks = [i for i in banks]
    max_ind = choose_index_bank(copy_banks)
    blocks_to_move = copy_banks[max_ind]
    copy_banks[max_ind] = 0
    i = max_ind + 1

    while blocks_to_move != 0:
        if i == len(copy_banks):
            i = 0
        copy_banks[i] += 1
        i += 1
        blocks_to_move -= 1

    return copy_banks


def reallocation(puzzle):
    seen_states = []
    cycles = 0
    while puzzle not in seen_states:
        seen_states.append(puzzle)
        puzzle = distribute_blocks(puzzle)
        cycles += 1
    return cycles


def reallocation_part2(puzzle):
    seen_states = []
    cycles = 0
    while puzzle not in seen_states:
        seen_states.append(puzzle)
        puzzle = distribute_blocks(puzzle)
        cycles += 1
    return abs(seen_states.index(puzzle) - cycles)


# Tests
assert choose_index_bank([0, 2, 7, 0]) == 2
assert choose_index_bank([2, 4, 1, 2]) == 1
assert choose_index_bank([3, 1, 2, 3]) == 0
assert choose_index_bank([0, 2, 3, 4]) == 3
assert distribute_blocks([0, 2, 7, 0]) == [2, 4, 1, 2]
assert distribute_blocks([2, 4, 1, 2]) == [3, 1, 2, 3]
assert distribute_blocks([3, 1, 2, 3]) == [0, 2, 3, 4]
assert distribute_blocks([0, 2, 3, 4]) == [1, 3, 4, 1]
assert distribute_blocks([1, 3, 4, 1]) == [2, 4, 1, 2]
assert reallocation([0, 2, 7, 0]) == 5
assert reallocation_part2([0, 2, 7, 0]) == 4

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = list(map(int, f.readline().split()))
    print('Part1: ', reallocation(puzzle))
    print('Part2: ', reallocation_part2(puzzle))
