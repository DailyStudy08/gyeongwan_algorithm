word = input()
sub = input()
cnt = 0
i = 0
while i <= (len(word)-len(sub)):
    if word[i:i+len(sub)] == sub:
        cnt += 1
        i += len(sub)
    else:
        i += 1
print(cnt)