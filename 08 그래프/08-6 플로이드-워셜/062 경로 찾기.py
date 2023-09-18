n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

for k in range(n):
    for s in range(n):
        for e in range(n):
            if a[s][k] == 1 and a[k][e] == 1:
                a[s][e] = 1

for s in range(n):
    for e in range(n):
        print(a[s][e], end = ' ')
    print()
