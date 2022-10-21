def maximum(cnt, now):
    global max_sum
    if now > M:
        return
    if cnt == 3:
        if now > max_sum:
            max_sum = now
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            maximum(cnt+1, now + arr[i])
            visit[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
visit = [0] * N
maximum(0, 0)
print(max_sum)