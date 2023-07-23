import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum_numbers = [0]
tmp = 0

for i in numbers:
    tmp = tmp + i
    sum_numbers.append(tmp)

for i in range(m):
    s, e = map(int, input().split())
    print(sum_numbers[e] - sum_numbers[s-1])
