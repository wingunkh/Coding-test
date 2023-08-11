import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = False

def DFS(v, d):
    global result
    
    if d == 5:
        result = True
        return
    
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i, d+1)
    visited[v] = False
    
for i in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    DFS(i, 1)
    if result == True:
        print(1)
        break
else:
    print(0)
