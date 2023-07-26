import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0

for i in range(n):
    target = a[i]
    left= 0
    right = n - 1

    while left < right:
        if a[left] + a[right] < target:
            left += 1
        elif a[left] + a[right] > target:
            right -= 1
        else:
            if left != i and right != i:
                cnt += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1

print(cnt)
