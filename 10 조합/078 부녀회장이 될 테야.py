t = int(input())
d = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    d[0][i] = i
    d[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        d[i][j] = d[i][j-1] + d[i-1][j]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(d[k][n])
