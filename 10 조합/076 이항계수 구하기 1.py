n, k = map(int, input().split())
d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    d[i][0] = 1 # i개 중 1개도 선택하지 않는 경우의 수는 1개
    d[i][1] = i # i개 중 1개를 뽑는 경우의 수는 i개
    d[i][i] = 1 # i개 중 i개를 선택하는 경우의 수는 1개 

for i in range(n+1):
    for j in range(1, i):
        d[i][j] = d[i-1][j] + d[i-1][j-1] # 조합 점화식
        
print(d[n][k])
