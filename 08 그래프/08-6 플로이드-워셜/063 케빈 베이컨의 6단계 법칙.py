import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
score = sys.maxsize
answer = 0

for i in range(1, n+1):
    a[i][i] = 0

for i in range(m):
    s, e = map(int, input().split())
    a[s][e] = 1
    a[e][s] = 1

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if a[s][e] > a[s][k] + a[k][e]:
                a[s][e] = a[s][k] + a[k][e]
                
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        sum += a[i][j]
    if sum < score:
        score = sum
        answer = i
            
print(answer)
