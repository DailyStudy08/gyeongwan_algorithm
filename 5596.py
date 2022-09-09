arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
max_1 = 0
max_2 = 0
for i in arr_1:
    max_1 += i
for j in arr_2:
    max_2 += j
if max_1 >= max_2:
    result = max_1
else:
    result = max_2
print(result)