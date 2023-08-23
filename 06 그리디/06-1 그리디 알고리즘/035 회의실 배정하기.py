import sys
input = sys.stdin.readline

n = int(input())
a = []
buff = 0
count = 0

for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

# 종료 시간(e) 기준으로 오름차순 정렬
# 종료 시간(e)이 같을 때 사작 시간(s)을 기준으로 오름차순 정렬
a.sort(key = lambda x: (x[1], x[0]))

for start, end in a:
    if start >= buff:
        count += 1
        buff = end

print(count)
