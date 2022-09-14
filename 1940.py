N = int(input())
M = int(input())
arr = list(map(int,input().split()))
lst = sorted(arr)
cnt = 0
i = 0
j = N-1
while i < j:
    if lst[i] + lst[j] == M:
        cnt += 1
        i += 1
        j -= 1
    elif lst[i] + lst[j] < M:
        i += 1
    else:
        j -= 1
print(cnt)