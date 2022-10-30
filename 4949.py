while True:
    word = input()
    result = True
    if word == '.':
        break
    visit = []
    for i in word:
        if i == ')':
            if len(visit) == 0:
                result = False
                break
            if visit[len(visit)-1] != '(':
                result = False
                break
            else:
                visit.pop()
        if i == ']':
            if len(visit) == 0:
                result = False
                break
            if visit[len(visit)-1] != '[':
                result = False
                break
            else:
                visit.pop()

        if i == '(' or i == '[':
            visit.append(i)
    if len(visit) != 0:
        result = False
    if result:
        print('yes')
    else:
        print('no')