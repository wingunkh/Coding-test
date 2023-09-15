import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * k for _ in range(n+1)]
q = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

distance[1][0] = 0
heapq.heappush(q, (0, 1))

while q:
    cost, now = heapq.heappop(q)
    
    for next, weight in a[now]:
        sum = cost + weight # 현재 노드까지의 가중치 + 현재 노드에서 다음 노드까지의 가중치
        if distance[next][k-1] > sum:
            distance[next][k-1] = sum
            distance[next].sort()
            heapq.heappush(q, (sum, next))

for i in range(1,n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])
