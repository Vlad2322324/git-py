from random import randint

print("Первое задание")
k1 = randint(0, 100)
k2 = randint(0, 100)
k3 = randint(0, 100)
print("Числа:", k1, k2, k3, "Ср. ариф. - ", (k1 + k2 + k3) / 3, '\n')

print("Второе задание")
x = randint(10, 100)
y = randint(1, 9)
print(x, '/', y, '\n', 'Целая часть:', x // y, 'Остаток:', x % y, '\n')

print("Третье задание")
x = 234.765
print("x=", x)
print("1)", round(x, 2))
print("2)", int(round(x, 0)))
print("3)", str(x).zfill(11))

print("\n\nЧетвертое задание")
x = 23789
sum = 0
print(f"Число:{x}")
while x > 0:


    sum=(sum * 10) + x%10
    x//= 10

print(f"Перевернутое число:{sum}")
