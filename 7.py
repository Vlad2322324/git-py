import collections
import sys

print("Первое задание")
text = "hello, word of word"
print('Строка: ', text)
chars_popularity = collections.Counter(text)
del chars_popularity[' ']
del chars_popularity[',']

print(chars_popularity)

text = text.split()
words_popularity = collections.Counter(text)
print(words_popularity)

print("Второе задание")

d = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

number = 3999

res = ''
for arab, roman in d:
    while number >= arab:
        res += roman
        number -= arab
print(res)

print("Третье задание")
rates = {'Sberbank': 55.8, 'VTB24': 53.91}
temp_rate = 100
temp_bank = ''
for bank in rates:
    if temp_rate > rates[bank]:
        temp_rate = rates[bank]
        temp_bank = bank

print(temp_bank, '->', temp_rate)

print("Четвертое задание")
book = {'Petr': '546810', 'Katya': '241815'}    
new_book = {}
print(book)

for data in book:
    new_book[book[data]] = data

print(new_book)

print("Пятое задание")
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
book = {}
i = 0
for i in range(len(dates)):
    book[dates[i]] = rates[i]
print(book)

print("Шестое задание")

data = [
    "X.O",
    "X..",
    "OOX"
]
print(data)
print('Res:')
o_win = 0
x_win = 0
for i in range(3):
    for j in range(3):
        if data[i][j] == 'X':
            x_win += 1
        if data[i][j] == 'O':
            o_win += 1
    if o_win == 3:
        print('0')
        sys.exit()
    if x_win == 3:
        print('X')
        sys.exit()
    x_win = o_win = 0

for j in range(3):
    for i in range(3):
        if data[i][j] == 'X':
            x_win += 1
        if data[i][j] == 'O':
            o_win += 1
    if o_win == 3:
        print('0')
        sys.exit()
    if x_win == 3:
        print('X')
        sys.exit()
    x_win = o_win = 0

for i in range(3):
    if data[i][i] == 'X':
        x_win += 1
    if data[i][i] == 'O':
        o_win += 1
if o_win == 3:
    print('0')
    sys.exit()
if x_win == 3:
    print('X')
    sys.exit()
x_win = o_win = 0

for i in range(3):
    if data[i][2 - i] == 'X':
        x_win += 1
    if data[i][2 - i] == 'O':
        o_win += 1
if o_win == 3:
    print('0')
    sys.exit()
if x_win == 3:
    print('X')
    sys.exit()
print('D')
