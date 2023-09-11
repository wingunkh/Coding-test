import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for i in range(1, n+1):
    buff = list(map(int, input().split()))[:-1]
    time[i] = buff[0]

    for j in buff[1:]:
        a[j].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result[now] += time[now]

    for next in a[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, n+1):
    print(result[i])
