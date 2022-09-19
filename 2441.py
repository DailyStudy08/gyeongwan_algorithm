N = int(input())
result = ''
for i in range(N, 0, -1):
    result = (N-i) * ' ' + i * '*'
    print(result)
