import sys
input = sys.stdin.readline

# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

n, m, k = map(int, input().split())
treeHeight = 0
tmp = n

while tmp > 0:
    tmp //= 2
    treeHeight += 1

# 트리 리스트의 크기 = 2^k >= N을 만족하는 k의 최솟값을 구한 후 2^(k+1)
treeSize = 2 ** (treeHeight + 1)
startIdx = treeSize // 2
tree = [0 for _ in range(treeSize + 1)]

for i in range(startIdx, startIdx + n):
    tree[i] = int(input())
    
tmp = treeSize - 1

while tmp != 1:
    tree[tmp // 2] += tree[tmp]
    tmp -= 1

for _ in range(m + k):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(s + startIdx - 1, e)
    else:
        s = s + startIdx - 1
        e = e + startIdx - 1
        print(getSum(s, e))
