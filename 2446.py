N = int(input())
arr = []
for i in range(N):
    print(i*' '+(N*2-1-2*i)*'*')
    if i == N-1:
        break
    arr.append(i * ' ' + (N * 2 - 1 - 2 * i) * '*')
for j in arr[::-1]:
    print(j)