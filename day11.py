def shortest_path(g1: tuple, g2: tuple, empty_rows: set, empty_columns: set, num_expansion: int):
    extra_space = len(empty_rows.intersection(set(range(g1[0], g2[0])))) + len(
        empty_columns.intersection(set(range(min(g1[1], g2[1]), max(g1[1], g2[1])))))
    return abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]) + extra_space * (num_expansion - 1)


def main():
    with open("day11.in") as data:
        grid = data.read().split("\n")

        rows = len(grid)
        columns = len(grid[0])

        empty_rows = set(range(rows))
        empty_columns = set(range(columns))

        # Find empty
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '#':
                    if i in empty_rows:
                        empty_rows.remove(i)
                    if j in empty_columns:
                        empty_columns.remove(j)

        # Find galaxies
        galaxies = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#':
                    galaxies.append(tuple((i, j)))

        sum_paths_1 = 0
        sum_paths_mil = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                sum_paths_1 += shortest_path(galaxies[i], galaxies[j], empty_rows, empty_columns, 1)
                sum_paths_mil += shortest_path(galaxies[i], galaxies[j], empty_rows, empty_columns, 1000000)

        print(sum_paths_1, sum_paths_mil)


if __name__ == '__main__':
    main()
