n, l, r = map(int, input().split())

d = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
d[1][1][1] = 1
mod = 1000000007

for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            d[i][j][k] = (d[i-1][j-1][k] + d[i-1][j][k-1] + d[i-1][j][k] * (i-2)) % mod
            # d[i-1][j-1][k] = 왼쪽에 빌딩을 추가할 때 이전 경우의 수
            # d[i-1][j][k-1] = 오른쪽에 빌딩을 추가할 때 이전 경우의 수
            # d[i-1][j][k] * (i-2) = 가운데에 빌딩을 추가할 때 이전 경우의 수

print(d[n][l][r])
