N = int(input())
arr = list(map(int, input().split()))
max_num = -1000000
min_num = 1000000
for i in range(N):
    if arr[i] > max_num:
        max_num = arr[i]
    if arr[i] < min_num:
        min_num = arr[i]
print(min_num, max_num)