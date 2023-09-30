n, k = map(int, input().split())
d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    d[i][1] = i
    d[i][0] = 1
    d[i][i] = 1

for i in range(n+1):
    for j in range(1, i):
        d[i][j] = (d[i-1][j] + d[i-1][j-1]) % 10007
        # 모듈러 연산의 특성 : (A % N + B % N) % N = (A + B) % N
        
print(d[n][k])
