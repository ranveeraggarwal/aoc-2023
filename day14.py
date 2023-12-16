def part_1(data):
    total_load = 0
    for col in range(len(data[0])):
        load = len(data)
        for row in range(len(data)):
            # print(load)
            if data[row][col] == "#":
                load = len(data[0]) - row - 1
            elif data[row][col] == "O":
                total_load += load
                load -= 1

    print(total_load)


def main():
    with open("day14.in") as data:
        data = data.read().split("\n")
        part_1(data)


if __name__ == '__main__':
    main()
