from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()
sum = 0

for i in range(n):
    pq.put(int(input()))

while pq.qsize() > 1:
    deck1 = pq.get()
    deck2 = pq.get()

    shuffled = deck1 + deck2

    sum += (shuffled)
    pq.put(shuffled)

print(sum)
