import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
distance = [sys.maxsize for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = PriorityQueue()

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

start, end = map(int, input().split())

distance[start] = 0
q.put((0, start))

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

print(distance[end])
