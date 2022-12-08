with open("input.txt") as f:
    lines = f.readlines()
    var_str = ''
    new_lines = []
    for x in lines:
        new_lines.append(x.replace('\n', ''))
    list_total = []
    for txt in new_lines:
        var_str = txt.split(',')
        list_total.append(var_str)
    list_new = []
    for x in list_total:
        for y in x:
            list_new.append(y.split('-'))
    totalScore = 0
    for i in range(len(list_new)):
        if i%2 == 0:
            if int(list_new[i+1][0]) <= int(list_new[i][0]) and int(list_new[i+1][1]) >= int(list_new[i][1]):
                totalScore += 1
            elif int(list_new[i+1][0]) >= int(list_new[i][0]) and int(list_new[i+1][1]) <= int(list_new[i][1]):
                totalScore += 1
    print(totalScore)
