import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
a = [[] for _ in range(V+1)]
distance = [sys.maxsize for _ in range(V+1)]
visited = [False for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append((v, w))

q.put((0, k)) # 우선순위 큐에 해당 노드까지의 거리와 노드의 번호 저장
distance[k] = 0

while q.qsize() > 0:
    _, now = q.get()
    if visited[now]:
        continue
    visited[now] = True

    for tmp in a[now]:
        next, weight = tmp
        if distance[next] > distance[now] + weight:
            distance[next] = distance[now] + weight
            q.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
