scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

winners = {
    'A': 'Z',  # Rock defeats Scissors
    'C': 'Y',  # Scissors defeats Paper
    'B': 'X',  # Paper defeats Rock
    'X': 'C',  # Rock defeats Scissors
    'Z': 'B',  # Scissors defeats Paper
    'Y': 'A',  # Paper defeats Rock
}

# invert the winners dictionary
losers = {v: k for k, v in winners.items()}


def get_strategy():
    strategy = []

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            opp, you = line.rstrip().split(' ')
            strategy.append((opp, you))

    return strategy


def one(strategy):
    score = 0

    for (opp, you) in strategy:
        score += scores[you]
        if winners[you] == opp:  # Win
            score += 6
        elif scores[you] == scores[opp]:  # Draw
            score += 3

    return score


def two(strategy):
    score = 0

    for (opp, you) in strategy:
        if you == 'Z':  # Win
            you = losers[opp]
            score += 6
        elif you == 'Y':  # Draw
            you = opp
            score += 3
        elif you == 'X':  # Lose
            you = winners[opp]

        score += scores[you]

    return score


if __name__ == '__main__':
    strategy = get_strategy()

    print(one(strategy))
    print(two(strategy))
