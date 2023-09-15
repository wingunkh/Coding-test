import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
distance = [sys.maxsize for _ in range(n+1)]
isNegativeCycle = False

for i in range(m):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

distance[1] = 0

for _ in range(n-1): # 특정 두 노드의 최단거리를 구성할 수 있는 엣지의 최대 개수 = 노드 개수 - 1
    for s, e, t in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

for s, e, t in edges:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
        isNegativeCycle = True
        break

if isNegativeCycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
