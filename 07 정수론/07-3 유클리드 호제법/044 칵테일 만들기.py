n = int(input())
array = [[] for _ in range(n)]
visited = [False] * n
result = [0] * n
lcm = 1 # 최소 공배수
mgcd = 1 # 최대 공약수

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    visited[v] = True

    for i in array[v]:
        next = i[0]
        if not visited[next]:
            result[next] = result[v] * i[2] // i[1]
            DFS(next)
    
for i in range(n-1):
    a, b, p, q = map(int, input().split())
    array[a].append((b, p, q))
    array[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 최소 공배수 = 두 수의 곱 / 최대 공약수

result[0] = lcm
DFS(0)
mgcd = result[0]

for i in range(1, n):
    mgcd = gcd(mgcd, result[i])

for i in range(n):
    print(int(result[i] // mgcd), end = ' ')
