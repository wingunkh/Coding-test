import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
buff = [0] * n
cnt = 0

def merge_sort(a, start, end):
    global cnt
    
    if start < end:
        center = (start + end) // 2

        merge_sort(a, start, center)
        merge_sort(a, center + 1, end)

        i = start
        p1, p2 = start, center + 1

        while p1 <= center and p2 <= end:
            if a[p1] > a[p2]:
                buff[i] = a[p2]
                i += 1
                p2 += 1
                cnt += (p2 - i)
            else:
                buff[i] = a[p1]
                i += 1
                p1 += 1

        buff[i:end + 1] = a[p1:center + 1] + a[p2:end + 1]

        for i in range(start, end + 1):
            a[i] = buff[i]

merge_sort(a, 0, len(a) - 1)

print(cnt)
