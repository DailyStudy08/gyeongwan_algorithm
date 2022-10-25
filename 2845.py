L, P = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in arr:
    result.append(i - L*P)
print(*result)