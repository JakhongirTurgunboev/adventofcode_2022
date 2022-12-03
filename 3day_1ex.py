with open("input.txt") as f:
    lines = f.readlines()
    total = ''
    new_lines = []
    for line in lines:
        new_lines.append(line.replace('\n', ''))
    for l in new_lines:
        for i in range(0, len(l)//2):
            if l[i] in l[len(l)//2:]:
                total += l[i]
                break

    totalScore = 0
    print(len(total))
    for x in total:
        if x.isupper():
            totalScore += (ord(x) - 38)
        else:
            totalScore += (ord(x) - 96)

    print(totalScore)