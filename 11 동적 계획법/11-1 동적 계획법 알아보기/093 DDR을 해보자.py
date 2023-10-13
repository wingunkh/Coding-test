import sys

def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(a-b) == 2:
        return 4
    else:
        return 3

a = list(map(int, input().split()))
n = len(a)-1
d = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
# d[i][l][r] = i번째 움직임 후 발 위치가 (l, r) 일 때 누적된 힘의 최소값
d[0][0][0] = 0
answer = sys.maxsize

for i in range(1, n+1):
    for l in range(5):
        for r in range(5):
            d[i][a[i-1]][r] = min(d[i][a[i-1]][r], d[i-1][l][r] + move(l, a[i-1]))
            d[i][l][a[i-1]] = min(d[i][l][a[i-1]], d[i-1][l][r] + move(r, a[i-1]))

for i in range(5):
    for j in range(5):
        answer = min(answer, d[n][i][j])

print(answer)
