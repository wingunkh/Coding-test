m = int(input())
d = list(map(int, input().split()))
prob = [0 for _ in range(m)]
answer = 0

k = int(input())
amount = sum(d)

for i in range(m):
    if d[i] >= k:
        prob[i] = 1
        for K in range(k):
            prob[i] *= (d[i] - K) / (amount - K)
        answer += prob[i]

print(answer)
