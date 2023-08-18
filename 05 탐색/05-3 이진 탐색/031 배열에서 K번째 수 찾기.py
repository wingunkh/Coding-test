n = int(input())
k = int(input())

start = 1
end = k
answer = 0

while start <= end:
    middle = (start + end) // 2
    count = 0

    for i in range(1, n+1):
        count += min(middle // i, n)

    if count < k: # 중앙값보다 작거나 같은 수의 개수가 K보다 작을 때
        start = middle + 1
    else: # 중앙값보다 작거나 같은 수의 개수가 K보다 크거나 같을 때
        answer = middle 
        end = middle -1

print(answer)
