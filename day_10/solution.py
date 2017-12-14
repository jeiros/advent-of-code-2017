"""
https://adventofcode.com/2017/day/10
"""
from functools import reduce


def apply_hash(input_list, length, current_pos):
    copy_input_list = [i for i in input_list]
    if length > len(input_list):
        raise ValueError('length is > than len(input_list)')

    list_to_reverse = []
    i = current_pos % len(input_list)
    while len(list_to_reverse) < length:
        list_to_reverse.append(copy_input_list[i])
        i += 1
        if i >= len(copy_input_list):
            i = 0
    reversed_list = list(reversed(list_to_reverse))

    i = current_pos % len(input_list)
    for j in range(len(reversed_list)):
        copy_input_list[i] = reversed_list[j]
        i += 1
        if i >= len(copy_input_list):
            i = 0

    return copy_input_list


def round_knot_hash(a_list, list_of_len, curr_pos=0, skip=0):
    copy_a_list = [i for i in a_list]
    for l in list_of_len:
        copy_a_list = apply_hash(copy_a_list, l, curr_pos)
        curr_pos += (l + skip)
        skip += 1
    return copy_a_list, curr_pos, skip


def dense_hash(a_list):
    chunks = [a_list[i * 16:(i + 1) * 16] for i in range(16)]
    dense_hash = ""
    for ch in chunks:
        dense = reduce(lambda i, j: i ^ j, ch)
        dense_hash += format(dense, 'x').zfill(2)
    return dense_hash


def get_dense_hash_str(input_str):
    new_lengths = []
    for char in input_str:
        new_lengths += [ord(char)]
    new_lengths += [17, 31, 73, 47, 23]
    the_list = list(range(256))
    c = 0
    sk = 0
    for _ in range(64):
        the_list, c, sk = round_knot_hash(the_list, new_lengths, c, sk)
    return dense_hash(the_list)


assert get_dense_hash_str('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert get_dense_hash_str('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert get_dense_hash_str('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert get_dense_hash_str('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

if __name__ == '__main__':
    # Part 1
    puzzle = [206, 63, 255, 131, 65, 80, 238, 157, 254, 24, 133, 2, 16, 0, 1, 3]
    solution, _, _ = round_knot_hash(list(range(256)), puzzle)
    print('Part 1: ', solution[0] * solution[1])
    # Part 2
    inp = '206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3'
    print('Part 2:', get_dense_hash_str(inp))
