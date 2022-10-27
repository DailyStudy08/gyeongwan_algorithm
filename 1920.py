N = int(input())
arr_N = list(map(int, input().split()))
arr_N = sorted(arr_N)
M = int(input())
arr_M = list(map(int, input().split()))

for i in arr_M:
    result = 0
    left = 0
    right = N-1

    while left <= right:
        now = (left + right) // 2
        if i == arr_N[now]:
            result = 1
            break
        elif i > arr_N[now]:
            left = now+1
        elif i < arr_N[now]:
            right = now-1
    print(result)