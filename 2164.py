N = int(input())
cnt = 2
while True:
    if N <= 2:
        print(N)
        break
    cnt *= 2
    if cnt >= N:
        print((N - cnt//2)*2)
        break