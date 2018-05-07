grid = [ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

raw_max = []
colum_max = []
sum = 0
new_sum = 0
l = len(grid)
for i in range(0,l,1):
    raw_max.append(max(grid[i]))
    maxv = 0
    for j in range(0,l,1):
        sum += grid[i][j]
        if maxv<grid[j][i]:
            maxv=grid[j][i]
    colum_max.append(maxv)


for i in range(0,l,1):
    for j in range(0,l,1):
        if grid[i][j] < raw_max[i] and grid[i][j] < colum_max[j]:
            if raw_max[i] <colum_max[j]:
                diff = raw_max[i] - grid[i][j]
            else:
                diff = colum_max[j] -grid[i][j]
            grid[i][j] += diff
        new_sum += grid[i][j]

print(new_sum-sum)
