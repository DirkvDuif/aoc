def calories():
    with open("./advent_code/input.txt", "r") as f:
        data = f.read()

    list_of_sums = []
    data = data.split("\n")
    sum = 0
    for data_point in data:
        if data_point:
            sum += int(data_point)
        else:
            list_of_sums.append(sum)
            sum = 0

    list_of_sums.sort()
    new_list = list_of_sums[-3:]
    new_sum = 0
    for integer in new_list:
        new_sum += integer
    print(new_sum)
    pass


if __name__ == '__main__':
    calories()
