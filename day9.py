def part1(sequence):
    diff_sequences = generate_until_zero(sequence)
    return sum([diff_sequence[-1] for diff_sequence in diff_sequences])


def part2(sequence):
    diff_sequences = generate_until_zero(sequence)
    diff = diff_sequences[0][-1]
    for diff_sequence in diff_sequences[1:]:
        diff = diff_sequence[0] - diff
    return diff


def generate_until_zero(sequence):
    if len(sequence) == 1 or sum(sequence) == 0:
        return [sequence]
    diff_sequence = []
    for i in range(1, len(sequence)):
        diff_sequence.append(sequence[i] - sequence[i - 1])
    return generate_until_zero(diff_sequence) + [sequence]


def main():
    with open("day9.in") as data:
        total_1 = 0
        total_2 = 0
        for line in data:
            total_1 += part1([int(i) for i in line.strip().split(" ")])
            total_2 += part2([int(i) for i in line.strip().split(" ")])
        print(total_1, total_2)


if __name__ == '__main__':
    main()
