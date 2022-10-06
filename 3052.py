numbers = set()

for i in range(10):
    numbers.add(int(input()) % 42)
print(len(numbers))