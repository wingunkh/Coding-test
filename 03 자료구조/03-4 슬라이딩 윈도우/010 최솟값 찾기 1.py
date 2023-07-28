from collections import deque
N, L = map(int, input().split())
d = deque()
a = list(map(int, input().split()))

for i in range(N):
    while d and d[-1][1] > a[i]:
        d.pop()

    d.append((i, a[i]))

    if d[0][0] == i - L:
        d.popleft()

    print(d[0][1], end = ' ')
