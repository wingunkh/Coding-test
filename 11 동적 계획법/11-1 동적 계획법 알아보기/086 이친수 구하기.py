n = int(input())
d = [[0 for _ in range(2)] for _ in range(91)]
# d[i][0] = i자리일 때 각각 끝자리가 0인 이친수의 개수
# d[i][1] = i자리일 때 각각 끝자리가 1인 이친수의 개수
d[1][1] = 1

for i in range(2, n+1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

print(d[n][0] + d[n][1])
