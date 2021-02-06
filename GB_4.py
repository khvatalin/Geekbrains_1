n = int(input())

s = 0
while n > 10:
    q = n % 10
    n = n // 10
    if q > s:
        s = q
print(s)
