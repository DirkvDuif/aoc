def count_complete_overlap():
    with open("./advent_code/advent-of-code-2022/day4/input.txt", "r") as input:
        data = input.read().split("\n")

    count = 0
    for line in data:
        line = line.split(",")
        elf1, elf2 = line[0].split("-"), line[1].split("-")
        set_elf1 = list(range(int(elf1[0]), int(elf1[1]) + 1))
        set_elf2 = list(range(int(elf2[0]), int(elf2[1]) + 1))
        if any(x in set_elf1 and x in set_elf2 for x in set_elf1):
            count += 1
        elif any(x in set_elf2 and x in set_elf1 for x in set_elf2):
            count += 1

    print(count)
    pass


if __name__ == "__main__":
    count_complete_overlap()
