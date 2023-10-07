n = int(input())
d = [[0 for _ in range(91)] for _ in range(2)]
# d[0][i] = i자리일 때 각각 끝자리가 0인 이친수의 개수
# d[1][i] = i자리일 때 각각 끝자리가 1인 이친수의 개수
d[1][1] = 1

for i in range(2, n+1):
    d[0][i] = d[0][i-1] + d[1][i-1]
    d[1][i] = d[0][i-1]

print(d[0][n] + d[1][n])
