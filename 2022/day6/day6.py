def find_sequence():
    with open("./advent_code/day6/input.txt") as f:
        data = f.read()
    # hjsjhf
    for index, _ in enumerate(data):
        chars = set(data[index:index+14])
        if len(chars) == 14:
            return index + 14
        pass
    # set([2, 3,5,7,5])


if __name__ == '__main__':
    print(find_sequence())
