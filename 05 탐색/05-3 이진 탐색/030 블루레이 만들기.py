n, m = map(int, input().split())
a = list(map(int, input().split()))
start = max(a)
end = sum(a)

while start <= end:
    pc = (start + end) // 2
    sum = 0
    count = 0

    for i in a:
        if sum + i > pc:
            count += 1
            sum = 0
        sum += i
    if sum != 0:
        count += 1

    if count > m:
        start = pc + 1
    else:
        end = pc - 1

print(start)
