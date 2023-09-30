import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                parent[0][next] = now
                depth[next] = depth[now] + 1

def LCA(a, b):
    if depth[a] > depth[b]: # b가 더 깊은 depth가 되도록 조정
        tmp = a
        a = b
        b = tmp

    for K in range(k, -1, -1): # depth 빠르게 맞추기
        if 2 ** K <= depth[b] - depth[a]:
            b = parent[K][b]

    for K in range(k, -1, -1): # 조상 빠르게 찾기
        if a == b:
            break
        if parent[K][a] != parent[K][b]:
            a = parent[K][a]
            b = parent[K][b]

    if a != b:
        return parent[0][a]
    else:
        return a

n = int(input())
tree = [[] for _ in range(n+1)]
k = 0

while 2 ** k < n:
    k += 1

parent = [[0 for _ in range(n+1)] for _ in range(k+1)] # 각 노드의 2^K번째 부모 노드를 저장하는 리스트
depth = [1 for _ in range(n+1)] # 각 노드의 깊이를 저장하는 리스트
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

BFS(1)

for K in range(1, k+1):
    for N in range(1, n+1):
        parent[K][N] = parent[K-1][parent[K-1][N]]
        
m = int(input())

for _ in range(m):
    s, e = map(int, input().split())
    print(str(LCA(s, e)))
    print("\n")
