import sys
input = sys.stdin.readline

def getMin(s, e):
    result = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            result = min(result, tree[s])
            s += 1
        if e % 2 == 0:
            result = min(result, tree[e])
            e -= 1
        s = s // 2
        e = e // 2
    return result

n, m = map(int, input().split())
treeHeight = 0
tmp = n

while tmp > 0:
    tmp //= 2
    treeHeight += 1

treeSize = 2 ** (treeHeight + 1)
startIdx = treeSize // 2
tree = [sys.maxsize for _ in range(treeSize + 1)]

for i in range(startIdx, startIdx + n):
    tree[i] = int(input())
    
tmp = treeSize - 1

while tmp != 1:
    if tree[tmp // 2] > tree[tmp]:
        tree[tmp // 2] = tree[tmp]
    tmp -= 1

for _ in range(m):
    s, e = map(int, input().split())
    
    s = s + startIdx - 1
    e = e + startIdx - 1
    print(getMin(s, e))
