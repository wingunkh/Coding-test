import sys
input = sys.stdin.readline

t = int(input())
d = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):
    d[i][0] = 1
    d[i][1] = i
    d[i][i] = 1

for i in range(31):
    for j in range(1, i):
        d[i][j] = d[i-1][j] + d[i-1][j-1]

for _ in range(t):
    a, b = map(int, input().split())
    print(d[b][a])
