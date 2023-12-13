def move_boxes():
    with open("./advent_code/day5/boxes.txt", "r") as input:
        boxes = input.read().splitlines()

    with open("./advent_code/day5/input.txt", "r") as input:
        lines = input.read().splitlines()

    points_of_interest = {}
    list_of_strings = [""]*9
    inverted_boxes = boxes[::-1]
    for line in inverted_boxes:
        for index, char in enumerate(line):
            if char.isnumeric():
                points_of_interest[index] = char
            if char.isalpha():
                list_of_strings[int(points_of_interest[index]) - 1] += char

    for line in lines:
        words = line.split(" ")
        amount, start, to = words[1], words[3], words[5]
        list_of_strings[int(to) - 1] += list_of_strings[int(start) - 1][- int(amount):]
        list_of_strings[int(start) - 1] = list_of_strings[int(start) - 1][:- int(amount)]
        pass

    string = ""
    for line in list_of_strings:
        string += line[-1]
    pass


if __name__ == '__main__':
    move_boxes()
