n, m = map(int, input().split())
a = [0] * (10000001)
count = 0

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    for j in range(i+i, len(a), i):
        a[j] = 0

for i in range(2, 10000001):
    if a[i] != 0:
        tmp = a[i]

        while a[i] <= m / tmp:
            if a[i] >= n / tmp:
                count += 1
            tmp = tmp * a[i]

print(count)
