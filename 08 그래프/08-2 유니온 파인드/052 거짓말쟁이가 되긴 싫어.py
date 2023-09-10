import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
truth = list(map(int, input().split()))
del truth[0]
party = [[] for _ in range(m)]
result = 0

for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]

for i in party:
    parentNode = i[0]
    for j in range(1, len(i)):
        union(parentNode, i[j])

for i in party:
    parentNode = i[0]
    for j in truth:
        if find(parentNode) == find(j):
            break
    else:
        result += 1

print(result)
