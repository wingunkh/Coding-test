def is_palindrome(number):
    number_str = str(number)
    s = 0
    e = len(number_str) - 1

    while s < e:
        if number_str[s] == number_str[e]:
            s += 1
            e -= 1
        else:
            return False
    else:
        return True

n = int(input())
a = [0] * 10000001

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    for j in range(i+i, len(a), i):
        a[j] = 0      

for i in range(n, len(a)):
    if a[i] and is_palindrome(i):
        print(i)
        break
