import sys
from queue import PriorityQueue
input = sys.stdin.readline

def convert(string):
    converted = []
    
    for i in string:
        if 'a' <= i <= 'z':
            converted.append(ord(i) - ord('a') + 1)
        elif 'A' <= i <= 'Z':
            converted.append(ord(i) - ord('A') + 27)
        else:
            converted.append(0)
    return converted

def find(a):
    if a == parent[a]:
        return a
    else:
        return find(parent[a])

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
            
n = int(input())
edges = PriorityQueue()
parent = [i for i in range(n+1)]
LANS = 0
count = 0
result = 0

for i in range(n):
    LAN = convert(input())
    LANS += sum(LAN)
    for j in range(n):
        if i != j and LAN[j] != 0:
            edges.put((LAN[j], i, j))

while edges.qsize() > 0:
    w, s, e = edges.get()
    if find(s) != find(e):
        union(s, e)
        count += 1
        result += w

if count == n-1:
    print(LANS - result)
else:
    print(-1)
