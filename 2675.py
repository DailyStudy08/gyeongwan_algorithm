T = int(input())
for tc in range(1, T+1):
    R, S = map(str, input().split())
    R = int(R)
    result = ''
    for i in S:
        result += i*R
    print(result)