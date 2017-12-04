from itertools import combinations

if __name__ == '__main__':
    password_list = []
    with open('input.txt', 'r') as f:
        for line in f:
            password_list.append(line)

    valid = 0
    valid_2 = 0
    for passwd in password_list:
        passwd_as_list = passwd.split()
        passwd_as_set = set(passwd_as_list)
        if len(passwd_as_set) == len(passwd_as_list):
            valid += 1
            strong = True
            for i, j in combinations(passwd_as_set, 2):
                if set(i) == set(j):
                    strong = False
            if strong:
                valid_2 += 1

    print('Part 1:', valid)
    print('Part 2:', valid_2)
