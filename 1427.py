N = input()
result = ''
lst = [0] * 10
for i in N:
    if i == '0':
        lst[0] += 1
    elif i == '1':
        lst[1] += 1
    elif i == '2':
        lst[2] += 1
    elif i == '3':
        lst[3] += 1
    elif i == '4':
        lst[4] += 1
    elif i == '5':
        lst[5] += 1
    elif i == '6':
        lst[6] += 1
    elif i == '7':
        lst[7] += 1
    elif i == '8':
        lst[8] += 1
    elif i == '9':
        lst[9] += 1

for i in range(len(lst)-1, -1, -1):
    result += lst[i] * str(i)
print(result)