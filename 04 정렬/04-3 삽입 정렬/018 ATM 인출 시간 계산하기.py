n = int(input())
p = list(map(int, input().split()))
s = []

for i in range(1, len(p)):
    j = i
    tmp = p[i]

    while j > 0 and p[j-1] > tmp:
        p[j] = p[j-1]
        j -= 1
    p[j] = tmp

s.append(p[0])

for i in range(1, n):
    s.append(s[i-1] + p[i])

print(sum(s))
