a = input().split('-')
answer = 0

for i in a[0].split('+'):
    answer += int(i)

for i in a[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)
