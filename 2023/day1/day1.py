import datetime
import re

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

strings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven":7,
    "eight": 8,
    "nine": 9
}
start = datetime.datetime.now()
total = 0

for line in lines:

    numbers_obj = {}

    for key, value in strings.items():

        match = re.finditer(key, line)
        if match:
            for m in match:
                pos = m.start()
                numbers_obj[pos] = value

    for idx, char in enumerate(line):
        if char.isdigit():
            numbers_obj[idx] = char

    sorted_idx = sorted(numbers_obj.keys())

    numbers_str = str(numbers_obj[sorted_idx[0]]) + str(numbers_obj[sorted_idx[-1]])
    total += int(numbers_str)

print(total)

end = datetime.datetime.now()
print(end-start)