x, y, w, h = map(int, input().split())
lst = [x, y, w-x, h-y]
min_lenth = 1001
for i in lst:
    if i < min_lenth:
        min_lenth = i
print(min_lenth)