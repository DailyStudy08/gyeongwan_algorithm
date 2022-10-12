N = input()
N_num = int(N)
min_range = N_num - (len(N) * 9)
result = 0
for i in range(min_range, N_num):
    if i < 1:
        continue
    now = i
    for j in str(i):
        if now > N_num:
            break
        now += int(j)
    if now == N_num:
        result = i
        break
print(result)