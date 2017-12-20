"""
https://adventofcode.com/2017/day/18
"""
import re
regexp = re.compile(r'(?P<inst>snd|set|add|mul|mod|rcv|jgz) (?P<register>\w)(?P<rest>.*)')


def parse_instruction(string):
    match = regexp.match(string)
    captures = match.groupdict()
    return captures


def is_int(string):
    try:
        n = int(string)
        return True
    except ValueError:
        return False


def build_status(list_of_instructions):
    state = {}
    for inst in list_of_instructions:
        match = parse_instruction(inst)
        if match['register'] not in state.keys():
            state[match['register']] = 0
    return state


def execute_code(list_of_instructions):
    status = build_status(list_of_instructions)
    i = 0

    while i < len(list_of_instructions):
        match = parse_instruction(list_of_instructions[i])
        m_inst = match['inst']
        m_reg = match['register']
        m_rest = match['rest'].strip()

        if is_int(m_rest):
            y = int(m_rest)
        else:
            try:
                y = status[m_rest]
            except KeyError:
                # This is either a snd or rcv operation
                # which do not have an m_rest group
                y = None

        if m_inst == 'snd':
            played_freq = status[m_reg]
            i += 1
        elif m_inst == 'set':
            status[m_reg] = y
            i += 1
        elif m_inst == 'add':
            status[m_reg] += y
            i += 1
        elif m_inst == 'mul':
            status[m_reg] *= y
            i += 1
        elif m_inst == 'mod':
            status[m_reg] = status[m_reg] % y
            i += 1
        elif m_inst == 'rcv':
            if status[m_reg] != 0:
                recovered_freq = played_freq
                return recovered_freq
            i += 1
        elif m_inst == 'jgz':
            if status[m_reg] > 0:
                i += y
            else:
                i += 1


example = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

assert execute_code(example.split('\n')) == 4


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle = f.read()
    print('Part 1:', execute_code(puzzle.split('\n')))
