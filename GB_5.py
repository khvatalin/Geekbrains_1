gain = int(input())
cost = int(input())

if gain > cost:
    print('OK')
else:
    print('Error')
if gain > cost:
    print(gain / cost)
    pers = int(input())
    print(gain / cost / pers)
else:
    print('Error')
