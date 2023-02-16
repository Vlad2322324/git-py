print('Первое задание')
x = 15
print('Число - ', x)

print('Результат: ', end='')
if x % 3 == 0:
    print('Fizz', end=" ")
if x % 5 == 0:
    print('Buzz')
print('\n')

print('Второе задание')
x = 230
print('Число - ', x)

print('Результат: ', end='')
if x % 2 != 0:
    print('Плохо')
elif x >= 2 & x <= 5 & x % 2 == 0:
    print('Неплохо')
elif x >= 6 & x <= 20 & x % 2 == 0:
    print('Так себе')
elif x > 20 & x % 2 == 0:
    print('Отлично')
print('\n')

print('Третье задание')
N = 45
print('Число - ', N)

print('Результат: ', end='')
k = 0
while k <= N:
    print(k, end="")
    k = k + 1
print('\n')

print('Четвертое задание')
str = "How are you? Eh, ok. Low or Lower? Ohhh."
print('Строка: ' + str)

print('Результат: ', end='')
i = 0
while i < len(str):
    if str[i].istitle():
        print(str[i], end="")
    i = i + 1
print('\n\n')

print('Пятое задание')
str = "He is 123 gd dfg man"
print('Строка: ' + str)

print('Результат: ', end='')
spase = 0
i = 0
while 1:
    if str[i].isdigit():
        spase = 0
    elif str[i] == ' ':
        spase += 1
    if spase == 3:
        print(True)
        break
    if i == len(str) - 1:
        print(False)
        break
    i += 1

print('\n\n')

print('Шестое задание')
str = ["bright aright", "ok"]
print('Строки: ', str)

i = 0
print('Результат: ', end='')
while i < len(str):
    if i == len(str) - 1:
        print(str[i].replace("right", "left"))
    else:
        print(str[i].replace("right", "left"), end=',')
    i += 1
