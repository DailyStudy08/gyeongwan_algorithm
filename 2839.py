N = int(input())
cnt = 0
while True:
    if N == 0:
        break
    if N % 5 == 0:
        N -= 5
        cnt += 1
        continue
    elif N % 3 == 0:
        N -= 3
        cnt += 1
        continue
    if N >= 5:
        N -= 5
        cnt += 1
        continue
    elif 3 <= N < 5:
        N -= 3
        cnt += 1
        continue
    elif 1 <= N < 3:
        cnt = -1
        break
print(cnt)