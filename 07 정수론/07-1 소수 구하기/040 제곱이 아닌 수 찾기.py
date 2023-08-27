min, max = map(int, input().split())
square = [i**2 for i in range(2, int(max ** 0.5)+1)] # max보다 작은 모든 제곱 수
check = [1] * (max-min+1) # 제곱 수의 배수를 제거할 정답 리스트

for i in square: # 제곱 수를 하나씩 가져와서 반복
    x = min // i * i # 제곱 수의 최초 값이 min 보다 크도록 설정

    while x <= max:
        if x >= min:
            check[x-min] = 0 # 제곱 수의 배수를 정답 리스트에서 제거
        x += i # 제곱 수의 최초 값이 min 보다 크도록 설정

print(sum(check))
