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
                parent[next] = now
                depth[next] = depth[now] + 1

def LCA(a, b):
    if depth[a] < depth[b]:
        tmp = a
        a = b
        b = tmp

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a
        
n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)] # 각 노드의 부모 노드를 저장하는 리스트
depth = [1 for _ in range(n+1)] # 각 노드의 깊이를 저장하는 리스트
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

BFS(1)
m = int(input())

for _ in range(m):
    s, e = map(int, input().split())
    print(str(LCA(s, e)))
    print("\n")
