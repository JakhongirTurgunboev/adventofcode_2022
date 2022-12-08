with open("input.txt") as f:
    lines = f.readlines()
    total = ''
    new_lines = []
    for line in lines:
        if "move" in line:
            new_lines.append(line.replace('\n', ''))

    stackList = [['D', 'B', 'J', 'V'],
                 ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
                 ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
                 ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
                 ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
                 ['R', 'D', 'B', 'S', 'N', 'G'],
                 ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
                 ['W', 'L', 'F'],
                 ['S', 'V', 'F', 'M', 'R']]


    #stackList[0].append(stackList[4].pop())

    for i in new_lines:
        sub1 = "move "
        sub2 = " from"

        # getting index of substrings
        idx1 = i.index(sub1)
        idx2 = i.index(sub2)

        # length of substring 1 is added to
        # get string from next character
        res = i[idx1+len(sub1) - 1:idx2]

        counter = int(res)

        sub3 = "from "
        sub4 = " to"

        idx3 = i.index(sub3)
        idx4 = i.index(sub4)

        res2 = i[idx3+len(sub1) - 1:idx4]
        from_int = int(res2)

        to_int = int(i[len(i)-1: len(i)])

        slice = stackList[from_int-1][len(stackList[from_int-1])-counter:len(stackList[from_int-1])]
        stackList[to_int-1] = stackList[to_int-1] + slice
        stackList[from_int-1] = stackList[from_int-1][0:len(stackList[from_int-1])-counter]

    print(stackList)