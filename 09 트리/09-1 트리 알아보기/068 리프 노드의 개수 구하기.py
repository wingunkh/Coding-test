import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v):
    global answer
    hasChild = False
    visited[v] = True

    for i in a[v]:
        if not visited[i] and i != target:
            hasChild = True
            DFS(i)
    if hasChild == False:
        answer += 1
            
n = int(input())
a = [[] for _ in range(n)]
visited = [False for _ in range(n)]
root = 0
answer = 0

parents = list(map(int, input().split()))

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        a[parents[i]].append(i)

target = int(input())

if target == root:
    print(0)
else:
    DFS(root)
    print(answer)
