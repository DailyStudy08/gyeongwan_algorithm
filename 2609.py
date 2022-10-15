a, b = map(int, input().split())
result = 1
while True:
    for i in range(2, max(a, b)+1):
        if a % i == 0 and b % i == 0:
            result *= i
            a = a // i
            b = b // i
            break
    else:
        break
print(result)
print(result*a*b)