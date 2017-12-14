"""
https://adventofcode.com/2017/day/8
"""
import re


def match_line(line):
    reg = re.compile(r'(?P<add>\w+) (?P<act>inc|dec) (?P<amo>\d+|-\d+) if (?P<add_cnd>\w+) (?P<cnd>.{1,2}) (?P<amo_cnd>\d+|-\d+)')
    match = reg.match(line)
    if match is not None:
        return match.groupdict()


def retrieve_states(list_of_matches):
    states = []
    for match in list_of_matches:
        add = match['add']
        if add not in states:
            states.append(add)
    return states


def execute_instructions(list_of_matches):
    state = dict.fromkeys(retrieve_states(list_of_matches), 0)
    for match in list_of_matches:
        if match['cnd'] == '==' and state[match['add_cnd']] == int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '>=' and state[match['add_cnd']] >= int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '<=' and state[match['add_cnd']] <= int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '>' and state[match['add_cnd']] > int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '<' and state[match['add_cnd']] < int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '!=' and state[match['add_cnd']] != int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
    largest_ind = max(list(state.values()))
    return largest_ind


def execute_instructions_2(list_of_matches):
    state = dict.fromkeys(retrieve_states(list_of_matches), 0)
    largest_ind = max(list(state.values()))
    for match in list_of_matches:
        if match['cnd'] == '==' and state[match['add_cnd']] == int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '>=' and state[match['add_cnd']] >= int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '<=' and state[match['add_cnd']] <= int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '>' and state[match['add_cnd']] > int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '<' and state[match['add_cnd']] < int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        elif match['cnd'] == '!=' and state[match['add_cnd']] != int(match['amo_cnd']):
            if match['act'] == 'inc':
                state[match['add']] += int(match['amo'])
            else:
                state[match['add']] -= int(match['amo'])
        largest_ind = max(largest_ind, max(list(state.values())))
    return largest_ind


example = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


assert execute_instructions([match_line(l) for l in example.split('\n')]) == 1
assert execute_instructions_2([match_line(l) for l in example.split('\n')]) == 10

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.readlines()

    print('Part 1:', execute_instructions([match_line(l) for l in puzzle]))
    print('Part 2:', execute_instructions_2([match_line(l) for l in puzzle]))
