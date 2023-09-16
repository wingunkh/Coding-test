import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())
edges = []
distance = [-sys.maxsize for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, -w))

city = list(map(int, input().split()))

distance[start] = city[start]

for i in range(n+101): # 양수 사이클 발견 시 연결된 모든 노드를 업데이트하기 위해 n+100회 반복
    for s, e, w in edges:
        if distance[s] == -sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e] = sys.maxsize
        elif distance[e] < distance[s] + city[e] + w:
            distance[e] = distance[s] + city[e] + w
            if i >= n-1: # 양수 사이클 발견
                distance[e] = sys.maxsize
            

if distance[end] == -sys.maxsize:
    print("gg")
elif distance[end] == sys.maxsize:
    print("Gee")
else:
    print(distance[end])
