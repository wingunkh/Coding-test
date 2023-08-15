import sys
from collections import deque
input = sys.stdin.readline

def DFS(v):
    print(v, end = ' ')
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    q = deque()
    
    q.append(v)
    print(v, end = ' ')
    visited[v] = True

    while q:
        node = q. popleft()

        for i in a[node]:
            if not visited[i]:
                q.append(i)
                print(i, end = ' ')
                visited[i] = True

n, m, v = map(int, input().split())
a = [[] for _ in range(n+1)] # 인접 리스트
visited = [False] * (n+1) # 방문 리스트
            
for i in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in  a:
    i.sort()

DFS(v)

print()
visited = [False] * (n+1)

BFS(v)
