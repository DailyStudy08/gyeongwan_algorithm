lst = []
idx = 0
max_num = 0
for i in range(9):
    lst.append(int(input()))
for i in range(len(lst)):
    if lst[i] > max_num:
        idx = i+1
        max_num = lst[i]
print(max_num)
print(idx)
