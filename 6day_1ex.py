with open("input.txt") as f:
    lines = f.readlines()
    total = ''
    new_lines = []
    counter = 0
    for line in lines:
        print(len(line))
        while counter in range(len(line)):
            if line[counter] not in new_lines:
                new_lines.append(line[counter])
                counter += 1
                if len(new_lines) == 4:
                    print(counter)
                    break
            else:
                index = new_lines.index(line[counter])
                counter -= ((len(new_lines)-1) - index)
                new_lines = []


