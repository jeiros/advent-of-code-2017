"""
https://adventofcode.com/2017/day/17
"""


def update_spinlock(numbers, pos, step, val_to_insert):
    new_pos = (pos + step) % len(numbers)
    numbers.insert(new_pos + 1, val_to_insert)
    return numbers, numbers.index(val_to_insert)


def apply_spinlock(step, iterations):
    nums = [0]
    ins = 1
    pos = 0
    for _ in range(iterations):
        nums, pos = update_spinlock(nums, pos, step, ins)
        ins += 1
    return nums


def circular_buffer(puzzle):
    nums = apply_spinlock(puzzle, 2017)
    index_2017 = nums.index(2017)
    i_find = (index_2017 + 1) % len(nums)
    return nums[i_find]


def part2(step, iterations):
    pos = 0
    for i in range(1, iterations):
        pos = (pos + step) % i
        if pos == 0:
            num_after0 = i
        pos += 1
    return num_after0


assert circular_buffer(3) == 638


if __name__ == '__main__':
    print('Part 1:', circular_buffer(312))
    # Part 2
    print('Part 2:', part2(312, 50000000))
