M = int(input())
key = 1
for _ in range(M):
    x, y = map(int, input().split())
    if x == key:
        key = y
    elif y == key:
        key = x
print(key)