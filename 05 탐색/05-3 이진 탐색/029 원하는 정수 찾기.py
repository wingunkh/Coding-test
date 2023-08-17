import sys
input = sys.stdin.readline

def binary_search(a, target):
    pl = 0
    pr = len(a) - 1

    while pl <= pr:
        pc = (pl + pr) // 2

        if target > a[pc]:
            pl = pc + 1
        elif target < a[pc]:
            pr = pc - 1
        else:
            print(1)
            break
    else:
        print(0)
    

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in b:
    binary_search(a, i)
