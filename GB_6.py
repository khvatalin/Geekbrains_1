marafon = int(input('Сколько километров на планируемом марафоне: '))
plan_day = int(input('Количество километров тренировки в первый день: '))
plan_perc = 10
day = 1

while marafon > plan_day:
    day += 1
    plan_day = plan_day + plan_day * (plan_perc / 100)
print(day, 'дней')