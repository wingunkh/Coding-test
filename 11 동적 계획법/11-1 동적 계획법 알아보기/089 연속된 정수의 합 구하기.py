n = int(input())
a = list(map(int, input().split()))
d = [[0 for _ in range(n)] for _ in range(2)]

d[0][0] = a[0]
d[1][0] = a[0]
# d[0][i] = 특정 원소를 제거하지 않는 경우, i+1번째 수를 포함하는 최대 연속 합
# d[1][i] = 특정 원소를 제거하는 경우, 최대 연속 합

for i in range(1, n):
    d[0][i] = max(a[i], d[0][i-1] + a[i])
    d[1][i] = max(d[0][i-1], d[1][i-1] + a[i])
    # d[0][i-1] = i+1번째 원소를 제거하는 경우
    # d[1][i-1] + a[i] = i+1번째 이전의 원소를 이미 제거한 경우

print(max(max(d[0]), max(d[1])))
