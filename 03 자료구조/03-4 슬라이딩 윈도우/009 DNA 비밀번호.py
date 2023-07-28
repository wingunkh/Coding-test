s, n = map(int, input().split())
a = list(input())
b = list(map(int, input().split()))
cnt = 0
left = 0
right = n - 1

a_count = a[left:right + 1].count('A')
c_count = a[left:right + 1].count('C')
g_count = a[left:right + 1].count('G')
t_count = a[left:right + 1].count('T')

while right < s:
    if a_count >= b[0] and c_count >= b[1] and g_count >= b[2] and t_count >= b[3]:
        cnt += 1

    left += 1
    right += 1

    if right == s:
        break

    if a[left - 1] == 'A':
        a_count -= 1
    elif a[left - 1] == 'C':
        c_count -= 1
    elif a[left - 1] == 'G':
        g_count -= 1
    else:
        t_count -= 1

    if a[right] == 'A':
        a_count += 1
    elif a[right] == 'C':
        c_count += 1
    elif a[right] == 'G':
        g_count += 1
    else:
        t_count += 1

print(cnt)
