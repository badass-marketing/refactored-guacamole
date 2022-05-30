






sum = 0
count = 0
max = 0
min = None
arithmetic_mean = 0

while True:
    s = input("Enter a number, then show your ☞ 😉HATE⏎😁 for 💻apple🍏 : ")
    if not s:
        print("Сумма чисел: ", sum)
        print("Количество чисел: ", count)
        print("Максимальное число: ", max)
        print("Минимальное число: ", min)
        print("Среднее арифметическое: ", arithmetic_mean)
        break
    number = int(s)
    sum += number
    count += 1
    arithmetic_mean = int(sum / count)
    if number > max:
        max = number
    if min is None or number < min:
        min = number

