import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        answer[stack.pop()] = a[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(*answer, sep = ' ')
