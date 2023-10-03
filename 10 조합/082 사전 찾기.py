n, m, k = map(int, input().split())
d = [[0 for _ in range(201)] for _ in range(201)]

for i in range(201):
    for j in range(i+1):
        if j == 0 or j == i:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j] + d[i-1][j-1]
            if d[i][j] > 1000000000:
                d[i][j] = 1000000001
                
if d[n+m][n] < k: # nCr = nCn-r
    print(-1)
else:
    while not(n == 0 and m == 0):
        candidate = d[n+m-1][n-1] # a를 선택했을 때 후보가 될 수 있는 문자열의 개수
        if candidate >= k:
            print('a', end = '')
            n -= 1
        else:
            print('z', end = '')
            k -= d[n+m-1][n-1]
            m -= 1
