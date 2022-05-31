


n = int(input("Введи число: "))

k = 0
for i in range(2, n // 2+1):
    if (n % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")

print("Список простых чисел: ")

def p(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
        else:
            return True

for i in range(2, n):
    if p(i) == True:
        print(i)


