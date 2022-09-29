A = int(input())
B = int(input())
C = int(input())
num = A*B*C
lst = [0] * 10
for i in str(num):
    lst[int(i)] += 1
for i in lst:
    print(i)