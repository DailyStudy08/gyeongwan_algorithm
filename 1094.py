X = int(input())
stick = 64
cnt = 0
while X > 0:
    if X < stick:
        stick = stick // 2
    elif X >= stick:
        X -= stick              # 값을 빼주는게 하나를 붙인 것.
        stick = stick // 2      # 앞선 stick값과는 비교가 끝났으니 다시 반으로 나눔.
        cnt += 1
print(cnt)