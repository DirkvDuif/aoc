with open("./2023/day3/input.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

total = 0
for i in range(len(lines)):
    digit = ""
    symbol_found = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            # WE HAVE FOUND A DIGIT
            digit += lines[i][j]
            # FIND SYMBOL
            for y in range(i - 1, i + 2):
                if not y < 0 and y < len(lines) :
                    for x in  range(j - 1, j + 2):
                        if not x < 0 and x < len(lines[i]):
                            if not lines[y][x] == "." and not lines[y][x].isdigit():
                                symbol = lines[y][x]
                                symbol_found = True
        else:
            if symbol_found == True and digit != "":
                total += int(digit)
            symbol_found = False
            digit = ""
    else:
        if symbol_found == True and digit != "":
            total += int(digit)
        symbol_found = False
        digit = ""
print(total)