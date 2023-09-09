import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)
    
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
parent = [i for i in range(n+1)]

for _ in range(m):
    isFind, a, b = map(int, input().split())

    if isFind:
        a = find(a)
        b = find(b)

        print("YES") if a == b else print("NO")
    else:
        union(a, b)
