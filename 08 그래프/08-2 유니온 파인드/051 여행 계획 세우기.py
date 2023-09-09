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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    cities = list(map(int, input().split()))

    for j in range(len(cities)):
        if cities[j]:
            union(i, j+1)
            
question = list(map(int, input().split()))

for i in range(1, m):
    if find(question[i]) != find(question[i-1]):
        print("NO")
        break
else:
    print("YES")
