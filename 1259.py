while True:
    num = list(map(int, input().strip()))
    if len(num) == 1 and num[0] == 0:
        break
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            print('no')
            break
    else:
        print('yes')
