while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    lst = sorted(lst)
    if lst[2]**2 == lst[1]**2 + lst[0]**2:
        print('right')
    else:
        print('wrong')