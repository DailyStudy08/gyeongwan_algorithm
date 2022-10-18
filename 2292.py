N = int(input())
if N == 1:
    print(1)
else:
    now = 1
    cnt = 0
    while True:
        cnt += 1
        if N <= now:
            print(cnt)
            break
        else:
            now += (6*cnt)
