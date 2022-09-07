A, B, V = map(int, input().split())

if V == A:                          # 정상 높이와 오르는 높이가 동일하면 하루가 걸림.
    result = 1
elif (V - A) % (A - B) == 0:        # 정상에 오르면 내려가지 않으니 V - A에 하루가 지난 상태인 (A - B)를 나누어 줌.
    result = (V - A) / (A - B) + 1  # V - A에 오르기만 한 날이 포함 되어있으니 + 1
else:
    result = (V - A) // (A - B) + 2 # 나머지가 있으면 하루 더 올라야하니 이전 조건 보다 + 1
print(int(result))