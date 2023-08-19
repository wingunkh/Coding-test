n, k = map(int, input().split())
a = []
count = 0

for i in range(n):
    a.append(int(input()))

for i in range(n-1, -1, -1):
    if a[i] <= k:
        count += int(k / a[i])
    k = k % a[i]

print(count)
