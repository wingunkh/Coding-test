import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0
left = 0
right = n - 1

while left < right:
    if a[left] + a[right] < m:
        left += 1
    elif a[left] + a[right] > m:
        right -= 1
    else:
        cnt +=1
        left += 1
        right -= 1

print(cnt)
