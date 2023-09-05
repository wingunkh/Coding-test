import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        
        for i in a[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result[i] += 1
            
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
best = 0
           
for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    BFS(i)

best = max(result)

for i in range(1, n+1):
    if result[i] == best:
        print(i, end = ' ')
