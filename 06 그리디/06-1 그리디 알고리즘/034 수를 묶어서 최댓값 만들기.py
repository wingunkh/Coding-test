from queue import PriorityQueue

n = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
zero = 0
one = 0
sum = 0

for i in range(n):
    data = int(input())

    if data > 1:
        plusPq.put(-data) # 우선순위 큐를 최소 힙이 아닌 최대 힙으로 구현
    elif data == 0:
        zero += 1
    elif data == 1:
        one += 1
    else:
        minusPq.put(data)

while plusPq.qsize() > 1:
    sum += (plusPq.get() * -1) * (plusPq.get() * -1)
else:
    if plusPq.qsize() == 1:
        sum += plusPq.get() * -1

while minusPq.qsize() > 1:
    sum += minusPq.get() * minusPq.get()
else:
    if minusPq.qsize() == 1:
        if zero == 0:
            sum += minusPq.get()

print(sum + one)
