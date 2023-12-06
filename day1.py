import sys


def find_value_1(puzzle):
    nums = [d for d in puzzle if d.isdigit()]
    return nums[0] + nums[-1]


def find_value_2(puzzle):
    num_values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}
    valid_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6",
                  "7", "8", "9"]
    min_indices = {}
    max_indices = {}
    for v in valid_nums:
        min_indices[v] = sys.maxsize
        max_indices[v] = -1
    for v in valid_nums:
        found_index_left = puzzle.find(v)
        found_index_right = puzzle.rfind(v)
        if found_index_left != -1:
            min_indices[v] = min(min_indices[v], found_index_left)
        if found_index_right != -1:
            max_indices[v] = max(max_indices[v], found_index_right)
    first = min(min_indices, key=min_indices.get)
    second = max(max_indices, key=max_indices.get)
    if valid_nums.index(first) < 9:
        first = num_values[first]
    if valid_nums.index(second) < 9:
        second = num_values[second]
    return first + second


def main():
    result = 0

    with open("day1.in") as puzzle:
        for line in puzzle:
            result += int(find_value_2(line))

    print(result)


if __name__ == '__main__':
    main()
