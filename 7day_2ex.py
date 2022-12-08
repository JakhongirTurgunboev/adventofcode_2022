from collections import defaultdict

SZ = defaultdict(int)

with open("input.txt") as f:
    lines = f.readlines()
    total = ''
    new_lines = []
    counter = 0
    output = 0
    result = 0
    path = []
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue

        else:
            try:
                sz = int(words[0])
                for i in range(len(path)+1):
                    SZ['/'.join(path[:i])] += sz
            except:
                pass

max_used = 70_000_000 - 30_000_000
total = SZ['/']
need_to_free = total - max_used
ans = 0
best = 1e9
for k, v in SZ.items():
    if v >= need_to_free:
        best = min(best, v)

    if v <= 100000:
        ans += v
print(best)
