with open("./day2/input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

score = 0

for line in lines:
    g_nmb, information = line.split(":")
    g_nmb = g_nmb.replace("Game ", "")
    sets = information.split(";")

    max_cubes = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            amount, color = cube.strip().split()

            max_cubes[color] = max(max_cubes[color], int(amount))

    game_score = 1

    for val in max_cubes.values():
        game_score *= val
    score += game_score

print(score)