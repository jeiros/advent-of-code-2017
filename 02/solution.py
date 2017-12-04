"""
http://adventofcode.com/2017/day/2
"""

from itertools import combinations


def checksum(list_of_rows):
    return sum(map(lambda row: max(row) - min(row), list_of_rows))


def checksum_divisibles(list_of_rows):
    output = 0
    for row in list_of_rows:
        for i, j in combinations(set(row), 2):
            if i % j == 0:
                output += int(i / j)
            elif j % i == 0:
                output += int(j / i)
    return output


test_spreadsheet = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8],
]

test_spreadsheet_part2 = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]

assert checksum(test_spreadsheet) == 18
assert checksum_divisibles(test_spreadsheet_part2) == 9

if __name__ == '__main__':
    vals = []
    with open('input.txt', 'r') as f:
        for line in f:
            vals.append(list(map(int, line.split())))
    print('part 1: ', checksum(vals))
    print('part 2: ', checksum_divisibles(vals))
