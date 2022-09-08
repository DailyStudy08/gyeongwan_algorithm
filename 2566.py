arr = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
row = 0
col = 0
for i in range(1, 10):
    for j in range(1, 10):
        if arr[i-1][j-1] >= max_num:
            max_num = arr[i-1][j-1]
            row = i
            col = j
print(max_num)
print(row, col)