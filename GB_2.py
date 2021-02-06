sec = int(input())

h = sec // 3600
m = (sec - (3600 * h)) // 60
s = sec - ((h * 3600) + (m * 60))
print('{:02}:{:02}:{:02}'.format(h, m, s))





