with open("./2023/day3/input.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

gears_found = {}

loc = ""
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
                            if lines[y][x] == "*":
                                loc = f"{y} {x}"
                                if not f"{y} {x}" in gears_found:
                                    gears_found[f"{y} {x}"] = []
                                symbol_found = True
        else:
            if symbol_found == True and digit != "":
                gears_found[loc].append(int(digit))
            symbol_found = False
            digit = ""
            loc = ""
    else:
        if symbol_found == True and digit != "":
            total += int(digit)
        symbol_found = False
        digit = ""


for v in gears_found.values():
    if len(v) == 2:
        total += v[0] * v[1]
print(total)