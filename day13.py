def is_mirror(pattern, mirror, tolerance=0):
    for row in pattern:
        left = row[:mirror]
        right = row[mirror:]
        if len(left) < len(right):
            right = right[: len(left)]
        elif len(left) > len(right):
            left = left[len(left) - len(right):]
        right = right[::-1]
        for i in range(len(left)):
            if left[i] != right[i]:
                tolerance -= 1
                if tolerance < 0:
                    return False
    if tolerance > 0:
        return False
    return True


def solve_part_1(pattern):
    for i in range(1, len(pattern[0])):
        if is_mirror(pattern, i):
            return i
    return 0


def solve_part_2(pattern):
    for i in range(1, len(pattern[0])):
        if is_mirror(pattern, i, 1):
            return i
    return 0


def get_transpose(pattern):
    return [''.join([row[i] for row in pattern]) for i in range(len(pattern[0]))]


def main():
    with open("day13.in") as data:
        data = data.read().split("\n\n")
        total_1 = 0
        total_2 = 0
        for pattern in data:
            pattern = pattern.split("\n")
            total_1 += solve_part_1(pattern) + 100 * solve_part_1(get_transpose(pattern))
            total_2 += solve_part_2(pattern) + 100 * solve_part_2(get_transpose(pattern))
    print(total_1, total_2)


if __name__ == '__main__':
    main()
