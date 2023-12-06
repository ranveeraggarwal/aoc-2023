import math


def get_symbols(puzzle):
    symbols = set()
    for row in puzzle:
        for cell in row:
            if cell.isdigit() or cell == '.':
                pass
            else:
                symbols.add(cell)
    return symbols


def get_num(puzzle, i, j, marked):
    if marked[i][j] or not puzzle[i][j].isdigit():
        return 0
    num = puzzle[i][j]
    marked[i][j] = True
    # go left
    j_left = j - 1
    while True:
        if not puzzle[i][j_left].isdigit():
            break
        num = puzzle[i][j_left] + num
        marked[i][j_left] = True
        j_left -= 1
    # go right
    j_right = j + 1
    while True:
        if not puzzle[i][j_right].isdigit():
            break
        num = num + puzzle[i][j_right]
        marked[i][j_right] = True
        j_right += 1
    return int(num)


def main():
    puzzle = []
    with open("day3.in") as data:
        for line in data:
            puzzle.append('.' + line.strip("\n") + '.')
    columns = len(puzzle[0])
    puzzle.insert(0, '.' * columns)
    puzzle.append('.' * columns)
    rows = len(puzzle)
    marked = [[False for _ in range(columns)] for _ in range(rows)]

    result_1 = 0
    result_2 = 0

    symbols = get_symbols(puzzle)

    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if puzzle[i][j] in symbols:
                relevant_numbers = [
                    get_num(puzzle, i - 1, j - 1, marked),
                    get_num(puzzle, i - 1, j, marked),
                    get_num(puzzle, i - 1, j + 1, marked),
                    get_num(puzzle, i, j - 1, marked),
                    get_num(puzzle, i, j + 1, marked),
                    get_num(puzzle, i + 1, j - 1, marked),
                    get_num(puzzle, i + 1, j, marked),
                    get_num(puzzle, i + 1, j + 1, marked),
                ]
                relevant_numbers = list(filter(lambda num: num > 0, relevant_numbers))
                result_1 += sum(relevant_numbers)
                if puzzle[i][j] == '*' and len(relevant_numbers) == 2:
                    result_2 += math.prod(relevant_numbers)
    print(result_1)
    print(result_2)


if __name__ == '__main__':
    main()