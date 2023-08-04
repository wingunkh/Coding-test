import sys
input = sys.stdin.readline

a = list(input())

for i in range(len(a)):
    max = i
    for j in range(i+1, len(a)):
        if a[j] > a[max]:
            max = j
    if a[i] < a[max]:
        a[i], a[max] = a[max], a[i]

print(*a, sep = '')
