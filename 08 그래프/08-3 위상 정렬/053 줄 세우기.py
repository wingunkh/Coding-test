import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end = ' ')

    for next in a[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
