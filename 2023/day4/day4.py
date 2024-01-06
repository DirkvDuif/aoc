from functools import lru_cache

# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

with open("./2023/day4/input.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

card_games = {}

@lru_cache(maxsize=None)
def get_game_numbers(lines) -> [str]:
    array = []
    for line in lines:
        game = line.split(":")
        array.append(game[0].strip())
    return array

# process lines into dict
for idx, line in enumerate(lines):
    game = line.split(":")
    game_number = game[0].strip()

    card_numbers = game[1].split("|")
    winning_numbers = set(card_numbers[0].strip().split())
    our_numbers = set(card_numbers[1].strip().split())

    card_games[game_number] = {"amount": 1, "numbers": [winning_numbers, our_numbers], "card_index": idx}

for k, v in card_games.items():
    for i in range(v["amount"]):
        winning_numbers = len(v["numbers"][1].intersection(v["numbers"][0]))
        games = get_game_numbers(tuple(lines[v["card_index"] + 1: v["card_index"] + 1 + winning_numbers]))
        for game in games:
            card_games[game]["amount"] += 1

total = sum([v["amount"] for v in card_games.values()])
print(total)
