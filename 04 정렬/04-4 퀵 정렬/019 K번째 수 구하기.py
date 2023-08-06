import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def quick_sort(a, left, right):
    pl = left
    pr = right
    pivot = a[(pl + pr) // 2]

    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while a[pr] > pivot:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
            
    if left < pr:
        quick_sort(a, left, pr)
    if pl < right:
        quick_sort(a, pl, right)

quick_sort(a, 0, len(a) - 1)

print(a[k-1])
