

a1 = int(input("Введите число -->:"))
# b2 = input("Введите целое число: ")
a2 = 0

while a1 > 0:
    dash = a1 % 10
    a1 = a1 // 10

    a2 = a2 * 10 + dash
print("Получите ответ -->: " + str(a2))



# b_list = list(b2)
# b_list.reverse()
# c2 = "".join(b_list)
# print("Обратное число: ", c2)
