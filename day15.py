def find_hash(word):
    initial = 0
    for c in word:
        initial = ((initial + ord(c)) * 17) % 256
    return initial


def main():
    with open("day15.in") as data:
        data = data.read().replace("\n", "").split(",")
        print(sum([find_hash(word) for word in data]))

        boxes = dict()
        for i in range(256):
            boxes[i] = list()

        for word in data:
            if "=" in word:
                word = word.split("=")
                box_num = find_hash(word[0])
                box_exists = False
                for box in boxes[box_num]:
                    if box[0] == word[0]:
                        box[1] = int(word[1])
                        box_exists = True
                        break
                if not box_exists:
                    boxes[box_num].append([word[0], int(word[1])])
            if "-" in word:
                word = word.split("-")
                box_num = find_hash(word[0])
                for box in boxes[box_num]:
                    if box[0] == word[0]:
                        boxes[box_num].remove(box)
                        break
        total_power = 0
        for i in boxes:
            for j, box in enumerate(boxes[i]):
                total_power += (i + 1) * (j + 1) * box[1]

        print(total_power)


if __name__ == '__main__':
    main()
