import numpy as np

with open("input.in", "r") as f:
    lines = f.read().strip().split()
print(lines)

grid = [list(map(int, list(line))) for line in lines]

n = len(grid)
m = len(grid[0])

grid = np.array(grid)
dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0

for i in range(n):
    for j in range(m):
        h = grid[i, j]
        score = 1

        for di, dj in dd:
            ii, jj = i, j
            dist = 0
            ii += di
            jj += dj
            while(0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                dist += 1
                ii += di
                jj += dj

                if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                    dist += 1

            score *= dist
        ans = max(ans, score)

print(ans)


print(ans)