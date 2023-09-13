import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
reverse = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for i in range(m):
    s, e, t = map(int, input().split())
    a[s].append((e, t))
    reverse[e].append((s, t))
    indegree[e] += 1

start, end = map(int, input().split())

q = deque()
q.append(start)

while q:
    now = q.popleft()
    for next in a[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if indegree[next[0]] == 0:
            q.append(next[0])

print(result[end])

count = 0
visited = [False] * (n+1)
q.append(end)
visited[end] = True

while q:
    now = q.popleft()
    for next in reverse[now]:
        if result[next[0]] + next[1] == result[now]:
            count += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                q.append(next[0])

print(count)
