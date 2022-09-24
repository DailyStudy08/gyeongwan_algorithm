T = int(input())
for tc in range(1, T+1):
    word = input()
    now_cnt = 0
    result = 0
    for i in word:
        if i == 'O':
            now_cnt += 1
            result += now_cnt
        else:
            now_cnt = 0
    print(result)