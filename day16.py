def recurse(grid, energized, pos):
    stack = [pos]
    while True:
        if len(stack) == 0:
            return
        curr = stack.pop()
        i = curr[0]
        j = curr[1]
        direction = curr[2]
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            continue
        if energized[i][j][direction]:
            continue
        energized[i][j][direction] = True
        next_dirs = []
        if grid[i][j] == '.':
            next_dirs.append(direction)
        elif grid[i][j] == '-':
            if direction == 1 or direction == 3:
                next_dirs.append(direction)
            elif direction == 0 or direction == 2:
                next_dirs.append(1)
                next_dirs.append(3)
        elif grid[i][j] == '|':
            if direction == 0 or direction == 2:
                next_dirs.append(direction)
            elif direction == 1 or direction == 3:
                next_dirs.append(2)
                next_dirs.append(0)
        elif grid[i][j] == '/':
            if direction == 0:
                next_dirs.append(3)
            elif direction == 1:
                next_dirs.append(2)
            elif direction == 2:
                next_dirs.append(1)
            elif direction == 3:
                next_dirs.append(0)
        elif grid[i][j] == '\\':
            if direction == 0:
                next_dirs.append(1)
            elif direction == 1:
                next_dirs.append(0)
            elif direction == 2:
                next_dirs.append(3)
            elif direction == 3:
                next_dirs.append(2)
        for n in next_dirs:
            stack.append(get_next(i, j, n))


def get_next(i, j, direction):
    if direction == 0:
        return [i + 1, j, direction]
    if direction == 1:
        return [i, j + 1, direction]
    if direction == 2:
        return [i - 1, j, direction]
    if direction == 3:
        return [i, j - 1, direction]


def part1(grid):
    energized = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    recurse(grid, energized, [0, 0, 1])
    num_energized = 0
    for row in energized:
        for cell in row:
            if True in cell:
                num_energized += 1
    print(num_energized)


def part2(grid):
    max_num_energized = 0
    for i in range(len(grid)):
        energized = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        recurse(grid, energized, [i, 0, 1])
        num_energized = 0
        for row in energized:
            for cell in row:
                if True in cell:
                    num_energized += 1
        max_num_energized = max(max_num_energized, num_energized)
    for i in range(len(grid)):
        energized = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        recurse(grid, energized, [i, len(grid[0]) - 1, 3])
        num_energized = 0
        for row in energized:
            for cell in row:
                if True in cell:
                    num_energized += 1
        max_num_energized = max(max_num_energized, num_energized)
    for j in range(len(grid[0])):
        energized = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        recurse(grid, energized, [0, j, 2])
        num_energized = 0
        for row in energized:
            for cell in row:
                if True in cell:
                    num_energized += 1
        max_num_energized = max(max_num_energized, num_energized)
    for j in range(len(grid[0])):
        energized = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        recurse(grid, energized, [len(grid) - 1, j, 0])
        num_energized = 0
        for row in energized:
            for cell in row:
                if True in cell:
                    num_energized += 1
        max_num_energized = max(max_num_energized, num_energized)
    print(max_num_energized)


def main():
    with open("day16.in") as grid:
        grid = grid.read().split("\n")
        part1(grid)
        part2(grid)


if __name__ == '__main__':
    main()
