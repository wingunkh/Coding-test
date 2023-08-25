n, m = map(int, input().split())
a = [0] * (m+1)

for i in range(2, m+1):
    a[i] = i

for i in range(2, int(m ** 0.5)+1):
    if a[i] == 0:
        continue
    for j in range(i+i, m+1, i):
        a[j] = 0

for i in range(n, m+1):
    if a[i]:
        print(a[i])
