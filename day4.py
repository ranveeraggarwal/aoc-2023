def get_winning_points(line):
    return len(
        list(set(filter(lambda num: num != '', line[8:].split("|")[0].strip().split(" "))).intersection(
            set(filter(lambda num: num != '', line.split("|")[1].strip().split(" "))))))


def main():
    total_1 = 0
    wins_per_game = []
    with open("day4.in") as data:
        for line in data:
            winning_points_for_game = get_winning_points(line)
            wins_per_game.append(winning_points_for_game)
            # Part 1
            if winning_points_for_game > 0:
                total_1 += 2 ** (winning_points_for_game - 1)
        # Part 2
        instances = [1 for _ in range(len(wins_per_game))]
        for i, win in enumerate(wins_per_game):
            for j in range(win):
                instances[i + j + 1] += instances[i]

        print(total_1, sum(instances))


if __name__ == '__main__':
    main()
