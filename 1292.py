A, B = map(int, input().split())
lst = []
cnt = 0
for i in range(1, B+1):     # 빈 리스트 생성 후 조건에 맞제끔 숫자 추가.
    for _ in range(i):
        lst.append(i)
    if len(lst) >= B:       # A부터 B까지만 알면 되니 break문.
        break
for i in range(A, B+1):
    cnt += lst[i-1]         # 인덱스 0부터 시작이니 i-1.
print(cnt)