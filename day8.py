from math import lcm


def part1(directions, instructions):
    curr = 'AAA'
    direction = 0
    steps = 0
    while curr != 'ZZZ':
        steps += 1
        if directions[direction] == 'L':
            curr = instructions[curr][0]
        else:
            curr = instructions[curr][1]
        direction = (direction + 1) % len(directions)

    print(steps)


def part2(directions, instructions):
    step_possibilities = []
    for curr in instructions.keys():
        if curr[2] != 'A':
            continue
        direction = 0
        steps = 0
        while curr[2] != 'Z':
            steps += 1
            if directions[direction] == 'L':
                curr = instructions[curr][0]
            else:
                curr = instructions[curr][1]
            direction = (direction + 1) % len(directions)
        step_possibilities.append(steps)

    print(lcm(*step_possibilities))


def main():
    with open("day8.in") as data:
        data = data.read().split("\n")
        directions = data[0]
        instructions = dict()
        for line in data[2:]:
            line = line.split(" = ")
            instructions[line[0]] = line[1].replace(")", "").replace("(", "").replace(" ", "").split(",")
        part2(directions, instructions)


if __name__ == '__main__':
    main()
