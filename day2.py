import operator
from functools import reduce


def parse_game_one(un_parsed_input: str):
    # Game 1: 1 blue, 8 green; 14 green, 15 blue; 3 green, 9 blue; 8 green, 8 blue, 1 red; 1 red, 9 green, 10 blue
    color_max = {"red": 0, "blue": 0, "green": 0}
    turns = un_parsed_input.split(":")[1].split(";")
    for turn in turns:
        for color_num in turn.split(","):
            color = color_num.split(" ")[2].strip()
            color_max[color] = max(color_max[color], int(color_num.split(" ")[1]))
    return int(un_parsed_input.split(":")[0][5:]), color_max


def get_if_valid(parsed_game):
    color_dict = parsed_game[1]
    if color_dict["red"] > 12 or color_dict["green"] > 13 or color_dict["blue"] > 14:
        return 0
    return parsed_game[0]


def __main__():
    result_sum_part_1 = 0
    result_sum_part_2 = 0

    with open("day2.in") as game_input:
        for line in game_input:
            parsed_game = parse_game_one(line)
            result_sum_part_1 += get_if_valid(parsed_game)
            result_sum_part_2 += reduce(operator.mul, parsed_game[1].values(), 1)

    print(result_sum_part_1)
    print(result_sum_part_2)


__main__()
