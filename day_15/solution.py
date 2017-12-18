"""
https://adventofcode.com/2017/day/15
"""


def int_to32bit_binary(number):
    return '{0:032b}'.format(number)


def lowest_16(binary_string):
    return binary_string[-16:]


def pair_equal(number1, number2):
    n1_bin = int_to32bit_binary(number1)
    n2_bin = int_to32bit_binary(number2)
    return lowest_16(n1_bin) == lowest_16(n2_bin)


def num_generator(prev, factor):
    mult = prev * factor
    return mult % 2147483647


def num_generator_part2(prev, factor, divisor):
    mult = prev * factor
    value = mult % 2147483647
    if value % divisor == 0:
        return value
    else:
        return num_generator_part2(value, factor, divisor)


def get_sample(seedA, seedB, n):
    i = 0
    valA = num_generator(seedA, 16807)
    valB = num_generator(seedB, 48271)
    for _ in range(n):
        if pair_equal(valA, valB):
            i += 1
        valA, valB = num_generator(valA, 16807), num_generator(valB, 48271)
    return i


def get_sample_part2(seedA, seedB, n):
    i = 0
    valA = num_generator_part2(seedA, 16807, 4)
    valB = num_generator_part2(seedB, 48271, 8)
    for _ in range(n):
        if pair_equal(valA, valB):
            i += 1
        valA, valB = num_generator_part2(valA, 16807, 4), num_generator_part2(valB, 48271, 8)
    return i


assert get_sample(65, 8921, 5) == 1
assert get_sample(65, 8921, 40000000) == 588
assert get_sample_part2(65, 8921, 5000000) == 309

if __name__ == '__main__':
    seedA, seedB = 883, 879
    part1 = get_sample(seedA, seedB, 40000000)
    part2 = get_sample_part2(seedA, seedB, 5000000)
    print('Part 1:', part1)  # 609
    print('Part 2:', part2)  # 609