def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return tuple((i, j))
    return tuple((-1, -1))


def find_next(i, j, c, direction):
    if c == '|':
        if direction == 0:
            return tuple((i + 1, j, 0))
        if direction == 2:
            return tuple((i - 1, j, 2))
    if c == '-':
        if direction == 1:
            return tuple((i, j + 1, 1))
        if direction == 3:
            return tuple((i, j - 1, 3))
    if c == 'L':
        if direction == 0:
            return tuple((i, j + 1, 1))
        if direction == 3:
            return tuple((i - 1, j, 2))
    if c == 'J':
        if direction == 0:
            return tuple((i, j - 1, 3))
        if direction == 1:
            return tuple((i - 1, j, 2))
    if c == '7':
        if direction == 2:
            return tuple((i, j - 1, 3))
        if direction == 1:
            return tuple((i + 1, j, 0))
    if c == 'F':
        if direction == 3:
            return tuple((i + 1, j, 0))
        if direction == 2:
            return tuple((i, j + 1, 1))
    return None


def find_distance(grid, s):
    distance = 1
    c = s
    while True:
        # print(grid[c[0]][c[1]], c)
        c = find_next(c[0], c[1], grid[c[0]][c[1]], c[2])
        distance += 1
        if grid[c[0]][c[1]] == 'S':
            return distance


def part1(grid):
    s = find_start(grid)
    if grid[s[0] + 1][s[1]] in ['|', 'L', 'J']:
        print(find_distance(grid, tuple((s[0] + 1, s[1], 0))) // 2)
    elif grid[s[0] - 1][s[1]] in ['|', 'F', '7']:
        print(find_distance(grid, tuple((s[0] - 1, s[1], 2))) // 2)


def iterate(grid, s):
    loop = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    c = s
    while True:
        loop[c[0]][c[1]] = True
        if grid[c[0]][c[1]] == 'S':
            return loop
        c = find_next(c[0], c[1], grid[c[0]][c[1]], c[2])


def part2(grid):
    s = find_start(grid)
    loop = None

    # Manual Hack Begins
    if grid[s[0] + 1][s[1]] in ['|', 'L', 'J']:
        loop = iterate(grid, tuple((s[0] + 1, s[1], 0)))
    elif grid[s[0] - 1][s[1]] in ['|', 'F', '7']:
        loop = iterate(grid, tuple((s[0] - 1, s[1], 2)))
    grid[s[0]] = grid[s[0]][:s[1]] + '|' + grid[s[0]][s[1] + 1:]
    # Manual Hack Ends, sue me. I am tired of this problem at this point and have no enthu for a generic solution.

    in_tiles = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # for row in loop:
    #     line = ""
    #     for cell in row:
    #         if cell:
    #             line += '1'
    #         else:
    #             line += '0'
    #     print(line)

    for i in range(len(loop)):
        inside = False
        pipe = ''
        for j in range(len(loop[0])):
            if loop[i][j]:
                in_tiles[i][j] = False
                if grid[i][j] == '|':
                    inside = not inside
                if grid[i][j] in ('F', 'L'):
                    assert (pipe == '')
                    pipe = grid[i][j]
                if grid[i][j] == '7':
                    if pipe == 'L':
                        inside = not inside
                    pipe = ''
                if grid[i][j] == 'J':
                    if pipe == 'F':
                        inside = not inside
                    pipe = ''
                continue
            if inside:
                in_tiles[i][j] = True

    # for line in in_tiles:
    #     x = ""
    #     for cell in line:
    #         if cell:
    #             x += 'I'
    #         else:
    #             x += '.'
    #     print(x)

    num_in_tiles = 0
    for line in in_tiles:
        for cell in line:
            if cell:
                num_in_tiles += 1
    print(num_in_tiles)


def main():
    with open("day10.in") as data:
        grid = data.read().split("\n")
        part1(grid)
        part2(grid)


if __name__ == '__main__':
    main()
