def get_calories():
    calories = []

    with open(__file__.replace('.py', '.txt')) as f:
        subtotal = 0
        for line in f.readlines():
            if line == '\n':
                calories.append(subtotal)
                subtotal = 0
            else:
                subtotal += int(line)

    # account for last line
    calories.append(subtotal)

    return calories


def one(calories):
    return max(calories)


def two(calories):
    # return the 3 largest values
    return sum(sorted(calories)[-3:])


if __name__ == '__main__':
    calories = get_calories()

    print(one(calories))
    print(two(calories))
