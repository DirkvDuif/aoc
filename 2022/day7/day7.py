def calc_dir_size():
    with open("./advent_code/day7/input.txt", "r") as input:
        data = input.read().split("\n")

    dict_of_directories = {}
    global current_dir
    current_dir = ""

    list_of_directories = []
    for line in data:
        current = line.split(" ")
        if current[0] == "$":
            if current[1] == "ls":
                continue
            elif current[1] == "cd":
                if current[2] == "..":
                    current_dir = list_of_directories.pop()
                else:
                    current_dir == current[2]
                    list_of_directories.append(current[2])

        elif current[0] == "dir":
            dict_of_directories[current[1]] = {}

        elif current[0].isalpha():
            pass

    pass


if __name__ == '__main__':
    calc_dir_size()
