from functools import cmp_to_key


def fix_hand(hand):
    return hand.replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('J', 'V').replace('T', 'U')


def fix_hand_with_weak_joker(hand):
    return hand.replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('J', '1').replace('T', 'U')


def get_score(hand):
    counts = sorted([hand.count(element) for element in set(hand)])
    if counts[-1] == 5:
        return 6
    if counts[-1] == 4:
        return 5
    if counts[-1] == 3 and counts[-2] == 2:
        return 4
    if counts[-1] == 3:
        return 3
    if counts[-1] == 2 and counts[-2] == 2:
        return 2
    if counts[-1] == 2:
        return 1
    return 0


def get_score_with_special_joker(hand):
    joker_count = 0
    counts = list()
    for element in set(hand):
        if element == '1':
            joker_count = hand.count(element)
        else:
            counts.append(hand.count(element))

    if len(counts) == 0:
        counts.append(joker_count)
    else:
        counts = sorted(counts)
        counts[-1] += joker_count

    if counts[-1] == 5:
        return 6
    if counts[-1] == 4:
        return 5
    if counts[-1] == 3 and counts[-2] == 2:
        return 4
    if counts[-1] == 3:
        return 3
    if counts[-1] == 2 and counts[-2] == 2:
        return 2
    if counts[-1] == 2:
        return 1
    return 0


def compare(hand_1: tuple, hand_2: tuple):
    if hand_1[1] > hand_2[1]:
        return 1
    if hand_1[1] < hand_2[1]:
        return -1
    if hand_1[1] == hand_2[1]:
        for i in range(len(hand_1[0])):
            if hand_1[0][i] > hand_2[0][i]:
                return 1
            if hand_1[0][i] < hand_2[0][i]:
                return -1
    return 0


def part1(data):
    hands = [[fix_hand(hand[0]), hand[1]] for hand in data]
    hands = [tuple((hand[0], get_score(hand[0]), int(hand[1]))) for hand in hands]
    cmp_key = cmp_to_key(compare)
    hands.sort(key=cmp_key)
    total = 0
    for i, hand in enumerate(hands):
        total += (i + 1) * hand[2]
    print(total)


def part2(data):
    hands = [[fix_hand_with_weak_joker(hand[0]), hand[1]] for hand in data]
    hands = [tuple((hand[0], get_score_with_special_joker(hand[0]), int(hand[1]))) for hand in hands]
    cmp_key = cmp_to_key(compare)
    hands.sort(key=cmp_key)
    total = 0
    for i, hand in enumerate(hands):
        total += (i + 1) * hand[2]
    print(total)


def main():
    with open("day7.in") as data:
        data = [line.split(" ") for line in data.read().split("\n")]
        part1(data)
        part2(data)


if __name__ == '__main__':
    main()
