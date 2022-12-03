with open("input.txt") as f:
    lines = f.readlines()
    total = ''
    new_lines = []
    for line in lines:
        new_lines.append(line.replace('\n', ''))
    for i in range(len(new_lines)):
        if (i+1) % 3 == 0:
            for x in new_lines[i]:
                if x in new_lines[i-1] and x in new_lines[i-2]:
                    total += x
                    break

    totalScore = 0
    print(len(total))
    for x in total:
        if x.isupper():
            totalScore += (ord(x) - 38)
        else:
            totalScore += (ord(x) - 96)

    print(totalScore)
