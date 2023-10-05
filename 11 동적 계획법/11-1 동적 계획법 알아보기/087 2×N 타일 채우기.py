n = int(input())
d = [0 for _ in range(1001)] # d[i] = 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
d[1] = 1
d[2] = 2
mod = 10007

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % mod

print(d[n])
