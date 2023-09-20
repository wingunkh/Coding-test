import sys
from collections import deque
from queue import PriorityQueue
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

def BFS(r, c, mark):
    q = deque()
    q.append((r, c))
    a[r][c] = mark
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for dy, dx in direct:
            y , x = r + dy, c + dx
            if 0 <= y < n and 0 <= x < m and a[y][x] and not visited[y][x]:
                a[y][x] = mark
                visited[y][x] = True
                q.append((y, x))

def build_bridge(y, x, start):
    for dy, dx in direct:
        y, x = y + dy, x + dx
        distance = 0

        while 0 <= y < n and 0 <= x < m:
            if a[y][x] == start:
                break
            if a[y][x] != 0:
                if distance > 1:
                    edges.put((distance, start, a[y][x]))
                break
            y, x = y + dy, x + dx
            distance += 1

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]

# 1. BFS를 통한 섬 구별
visited = [[False] * m for _ in range(n)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
mark = 1

for i in range(n):
    for j in range(m):
        if a[i][j] and not visited[i][j]:
            BFS(i, j, mark)
            mark += 1

# 2. 모든 다리 건설
edges = PriorityQueue()

for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
            build_bridge(i, j, a[i][j])

# 3. MST를 통한 다리 길이의 최솟값 출력
parent = [i for i in range(mark)]
count = 0
result = 0

while edges.qsize() > 0:
    w, a, b = edges.get()
    if find(a) != find(b):
        union(a, b)
        result += w
        count += 1

if count == mark - 2:
    print(result)
else:
    print(-1)
