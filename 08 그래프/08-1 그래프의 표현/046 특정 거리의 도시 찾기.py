import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    q = deque()

    q.append(v)
    visited[v] = True

    while q:
        node = q.popleft()

        for i in a[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer[i] = answer[node] + 1

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)
found = False

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

BFS(x)

for i in range(n):
    if answer[i] == k:
        found = True
        print(i)

if not found:
    print(-1)
