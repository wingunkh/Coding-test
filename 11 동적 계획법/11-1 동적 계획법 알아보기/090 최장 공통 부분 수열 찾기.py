import sys
input = sys.stdin.readline

a = [""] + list(input())
a.pop()
b = [""] + list(input())
b.pop()
d = [["" for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1] == b[i-1]:
            d[j][i] = d[j-1][i-1] + a[j-1]
        else:
            if len(d[j-1][i]) >= len(d[j][i-1]):
                d[j][i] = d[j-1][i]
            else:
                d[j][i] = d[j][i-1]

print(len(d[-1][-1]))
print(d[-1][-1])
