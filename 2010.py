N = int(input())
result = 1
for _ in range(N):
    multi = int(input())
    result += multi
result -= N
print(result)