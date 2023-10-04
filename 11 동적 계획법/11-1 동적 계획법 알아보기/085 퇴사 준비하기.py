n = int(input())
d = [0 for _ in range(n+2)] # d[i] = i번째 날부터 퇴사일까지 벌 수 있는 최대 수입
t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + t[i] <= n+1: # 해당 날짜의 상담이 가능할 때
        d[i] = max(d[i+1], p[i] + d[i + t[i]])
    else: # 해당 날짜의 상담이 불가능할 때
        d[i] = d[i+1]

print(d[1])
