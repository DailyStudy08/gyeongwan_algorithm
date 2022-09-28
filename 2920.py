lst = list(map(int, input().split()))
asc = 0
des = 0
for i in range(1, len(lst)):
    if lst[i] - lst[i-1] == 1:
        asc += 1
    if lst[i-1] - lst[i] == 1:
        des += 1
if asc == len(lst) - 1:
    print('ascending')
elif des == len(lst) - 1:
    print('descending')
else:
    print('mixed')