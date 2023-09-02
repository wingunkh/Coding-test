n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

stack = []
answer = []
next = 1

for i in range(n):
    target = a[i]

    if next <= target:
        while next <= target:
            stack.append(next)
            next += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        if stack.pop() == target:
            answer.append('-')
        else:
            print('NO')
            break
else:
    print(*answer, sep = '\n')
