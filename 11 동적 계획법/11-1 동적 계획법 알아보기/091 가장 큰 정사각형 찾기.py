import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [0 for _ in range(n)]
max = 0

for i in range(n):
    d[i] = list(map(int, input().rstrip()))

for i in range(1, n):
    for j in range(1, m):
        if d[i][j] == 1 and d[i-1][j] != 0 and d[i][j-1] != 0 and d[i-1][j-1] != 0:
            d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

for i in range(n):
    for j in range(m):
        if d[i][j] > max:
            max = d[i][j]
    
print(max * max)
