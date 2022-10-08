N = int(input())
lst = list(map(float, input().split()))
max_num = max(lst)
for i in range(N):
    lst[i] = lst[i] / max_num * 100
print(sum(lst)/N)