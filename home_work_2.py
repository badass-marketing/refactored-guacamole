
a = int(input("Введите количество детей в 1й группе: "))

b = int(input("Введите количество детей в 2й группе: "))

x = a
x1 = b

res1 = x // 2 + x % 2
res2 = x1 // 2 + x1 % 2

all_beds = int(res1 + res2)

print("Общее количество кроватей: ", all_beds)
