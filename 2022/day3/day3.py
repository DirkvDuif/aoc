def calc_priorities():
    with open("./advent_code/day3/input.txt", "r") as input:
        lines = input.read().split("\n")

    count = 0

    list_of_groups = zip(*(iter(lines),) * 3)
    for group in list_of_groups:
        set_1, set_2, set_3 = group
        char = set(set_1).intersection(set(set_2), set(set_3)).pop()
        if char.isupper():
            count += ord(char) - 38
            continue
        count += ord(char) - 96

    pass


if __name__ == "__main__":
    calc_priorities()
