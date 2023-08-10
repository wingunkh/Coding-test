import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)] # 인접 리스트
visited = [False] * (n+1) # 방문 리스트
cnt = 0

def DFS(v):
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

for i in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)
