import sys
input = sys.stdin.readline

def changeVal(index, value):
    tree[index] = value
    while index > 0:
        index = index // 2
        tree[index] = tree[index * 2] % MOD * tree[index * 2 + 1] % MOD

def getMul(s, e):
    partMul = 1
    while s <= e:
        if s % 2 == 1:
            partMul = partMul * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            partMul = partMul * tree[e] % MOD
            e -= 1
        s = s // 2
        e = e // 2
    return partMul

n, m, k = map(int, input().split())
treeHeight = 0
tmp = n
MOD = 1000000007

while tmp > 0:
    tmp //= 2
    treeHeight += 1

treeSize = 2 ** (treeHeight + 1)
startIdx = treeSize // 2
tree = [1 for _ in range(treeSize + 1)]

for i in range(startIdx, startIdx + n):
    tree[i] = int(input())
    
tmp = treeSize - 1

while tmp != 1:
    tree[tmp // 2] = tree[tmp // 2] * tree[tmp] % MOD
    tmp -= 1

for _ in range(m + k):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(s + startIdx - 1, e)
    else:
        s = s + startIdx - 1
        e = e + startIdx - 1
        print(getMul(s, e))
