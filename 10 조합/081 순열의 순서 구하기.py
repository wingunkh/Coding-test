import sys
input = sys.stdin.readline

f = [0] * 21 # 팩토리얼을 미리 계산해두기 위한 배열 f 
f[0] = 1
s = [0] * 21 # 결과 순열을 저장할 배열 s
visited = [False] * 21
n = int(input())

for i in range(1, n+1):
    f[i] = f[i-1] * i

tmp = list(map(int, input().split()))

if tmp[0] == 1:
    k = tmp[1]
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:
                continue
            if k <= cnt * f[n-i]:
                k -= (cnt-1) * f[n-i]
                s[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n+1):
        print(s[i], end = ' ')
else:
    k = 1
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, tmp[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * f[n-i]
        visited[tmp[i]] = True
    print(k)
