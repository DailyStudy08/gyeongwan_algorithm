T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())

    arr = [[0] * n for _ in range(k+1)]
    for i in range(n):
        arr[0][i] = i+1

    for i in range(k):

        for j in range(n):
            for l in range(j+1):
                arr[i+1][j] += arr[i][l]

    print(arr[k][n-1])
