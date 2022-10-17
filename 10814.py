N = int(input())
arr = []
for i in range(N):
    old, name = map(str, input().split())
    arr.append([int(old), name])
arr.sort(key=lambda x:x[0])
for i in range(N):
    print(arr[i][0], arr[i][1])