import sys
input= sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
S = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    row = [0] + list(map(int, input().split()))
    A.append(row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        S[i][j] = A[i][j] + S[i][j-1] + S[i-1][j] - S[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])
