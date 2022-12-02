with open("input.txt") as f:
    lines = f.readlines()
    new_lines = [[]]
    for line in lines:
        if line == '\n':
            new_lines.append([])
        else:
            line = line.replace("\n", "")
            line = int(line)
            new_lines[len(new_lines) - 1].append(line)

    newList = []
    for x in new_lines:
        newList.append(sum(x))

    print(max(newList))
