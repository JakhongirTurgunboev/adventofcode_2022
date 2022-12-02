with open("input.txt") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        if 'A X' in line:
            total += 4

        if 'A Y' in line:
            total += 8

        if 'A Z' in line:
            total += 3

        if 'B X' in line:
            total += 1

        if 'B Y' in line:
            total += 5

        if 'B Z' in line:
            total += 9

        if 'C X' in line:
            total += 7

        if 'C Y' in line:
            total += 2

        if 'C Z' in line:
            total += 6

    print(total)
