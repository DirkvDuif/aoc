loss = 0
tie = 3
win = 6

rock = 1
paper = 2
scissors = 3

# my_dict = {
#     "A": {
#         "X": tie + rock,
#         "Y": win + paper,
#         "Z": loss + scissors,
#     },
#     "B": {
#         "X": loss + rock,
#         "Y": tie + paper,
#         "Z": win + scissors,
#     },
#     "C": {
#         "X": win + rock,
#         "Y": loss + paper,
#         "Z": tie + scissors,
#     },
# }

my_dict = {
    "A": {
        "X": loss + scissors,
        "Y": tie + rock,
        "Z": win + paper,
    },
    "B": {
        "X": loss + rock,
        "Y": tie + paper,
        "Z": win + scissors,
    },
    "C": {
        "X": loss + paper,
        "Y": tie + scissors,
        "Z": win + rock,
    },
}


def calc_score():
    with open("./advent_code/day2/input.txt", "r") as input:
        data = input.read().split("\n")
    score = 0
    for line in data:
        opp, me = line.split(" ")
        score += my_dict[opp][me]

    return score


if __name__ == '__main__':
    calc_score()
