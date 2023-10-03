n = int(input())
d = [0] * 1000001
mod = 1000000000

d[1] = 0
d[2] = 1

for i in range(3, n+1):
    d[i] = (i-1) * (d[i-1] + d[i-2]) % mod

print(d[n])
