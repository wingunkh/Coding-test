import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v):
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            answer[i] = v
            DFS(i)
        
n = int(input())
a = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    a[n1].append(n2)
    a[n2].append(n1)

DFS(1)

for i in range(2, n+1):
    print(answer[i])
