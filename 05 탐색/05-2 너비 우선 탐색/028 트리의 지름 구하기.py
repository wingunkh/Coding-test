from collections import deque

def BFS(v):
    q = deque()

    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()

        for i in a[now]:
            if not visited[i[0]]:
                q.append(i[0])
                visited[i[0]] = True
                result[i[0]] = result[now] + i[1]

v = int(input())
a = [[] for _ in range(v+1)]
visited = [False] * (v+1)
result = [0] * (v+1)
maximun = 0

for i in range(v):
    data = list(map(int, input().split()))
    s = data[0]

    for j in range(1, len(data), 2):
        if data[j] == -1:
            break
        a[s].append((data[j], data[j+1]))

BFS(1)
maximum = result.index(max(result))

visited = [False] * (v+1)
result = [0] * (v+1)

BFS(maximum)
print(max(result))
