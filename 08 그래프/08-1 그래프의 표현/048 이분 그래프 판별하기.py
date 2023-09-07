import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v):
    global answer
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            check[i] = (check[v]+1)%2
            DFS(i)
        elif check[i] == check[v]:
            answer = False
    
n = int(input())
answer = True

for _ in range(n):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    check = [0 for _ in range(v+1)]
    answer = True

    for i in range(e):
        start, end = map(int, input().split())
        a[start].append(end)
        a[end].append(start)

    for i in range(1, v+1):
        if answer:
            DFS(i)
        else:
            print("NO")
            break
    else:
        print("YES")
