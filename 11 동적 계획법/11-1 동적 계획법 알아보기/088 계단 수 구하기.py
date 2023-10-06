n = int(input())
d = [[0 for _ in range(10)] for _ in range(101)]
# d[n][h] = 길이가 n인 계단에서 끝자리가 h로 종료되는 계단 수의 경우의 수
mod = 1000000000
sum = 0

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for j in range(1, 9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % mod

for i in range(10):
    sum = (sum + d[n][i]) % mod

print(sum)
