"""
https://adventofcode.com/2017/day/9
"""


def clean_group(group):
    group_clean = ''
    ignore = False
    inside_garbage = False
    canceled_count = 0
    for char in group:
        if not ignore:
            if char == '<' and not inside_garbage:
                inside_garbage = True
                canceled_count -= 1

            elif char == '!':
                ignore = True

            elif char == '>':
                inside_garbage = False

            if not inside_garbage and char in '{}':
                group_clean += char
            elif inside_garbage and char != '!':
                canceled_count += 1

        else:
            ignore = False

    return group_clean, canceled_count  # do not count first <


def get_score(group):
    cleaned_group, _ = clean_group(group)
    tot_score = 0
    level = 0
    for char in cleaned_group:
        if char == '{':
            level += 1
        elif char == '}':

            tot_score += level
            level -= 1
    return tot_score


assert get_score('{}') == 1.
assert get_score('{{{}}}') == 6.
assert get_score('{{},{}}') == 5.
assert get_score('{{{},{},{{}}}}') == 16.
assert get_score('{<a>,<a>,<a>,<a>}') == 1.
assert get_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9.
assert get_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9.
assert get_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3.


assert clean_group('<>')[1] == 0
assert clean_group('<random characters>')[1] == 17
assert clean_group('<<<<>')[1] == 3
assert clean_group('<{!>}>')[1] == 2
assert clean_group('<!!>')[1] == 0
assert clean_group('<!!!>>')[1] == 0
assert clean_group('<{o"i!a,<{i<a>')[1] == 10


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.readline()
    score = get_score(puzzle)
    _, canceled = clean_group(puzzle)
    print('Part 1:', score)
    print('Part 2:', canceled)
