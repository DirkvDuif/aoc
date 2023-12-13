with open("./day3/input.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

total = 0
for i in range(len(lines)):
    digit = ""
    symbol_found = False
    first = None
    last = None
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            # WE HAVE FOUND A DIGIT
            digit += lines[i][j]
            last = (i, j)
            if first is None:
                first = (i, j)
        else:
            if not first == None:
                for y in range(first[0] - 1, last[0] + 1):
                    if y < 0 or y > len(lines) - 1:
                        continue
                    for x in  range(first[1] - 1, last[1] + 1):
                        if x < 0 or x > len(lines[i]):
                            continue
                        if not lines[y][x] == "." and not lines[y][x].isdigit():
                            symbol_found = True
                if symbol_found == True and digit != "":
                    total += int(digit)
                    digit = ""
                    symbol_found = False
                    first, last = None, None

            digit = ""
            symbol_found = False
print(total)