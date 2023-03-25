print("Первое задание")
celsius = [39.2, 36.5, 37.3, 37.8]


def c_to_f(celsius):
    fahrenheit = []
    for c in celsius:
        fahrenheit.append((c * 9 / 5) + 32)
    return fahrenheit


print(c_to_f(celsius))

print("Второе задание")


def strlen(strarr):
    lenarr = []
    for name in strarr:
        lenarr.append(len(name))
    return lenarr


srtarr = ['Tina', 'Raj', 'Tom']
print(strlen(srtarr))

print("Третье задание")

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']
cap_count = sum(sentence.count('капитан') for sentence in sentences)
print(cap_count)

print("Четвертое задание")
X = [2, 3, 4]
Y = [10, 11, 12]


def arrdegree(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] ** b[i])
    return res


print(arrdegree(X, Y))

print("Пятое задание")


def f(n):
    res = []
    for x in range(n):
        if x == 0:
            res.append(-10)
        elif x % 3 != 0:
            res.append(45)
        elif x % 5 != 0:
            res.append(x / 5 + 93)
        else:
            res.append(x / 2)
    return res


n = 7
print(f(n))

print("Шестое задание")


def largest_histogram(histogram):
    temp_res = histogram[0]
    res = 0
    temp = 0
    for i in range(len(histogram)):
        temp = histogram[i]
        temp_res = histogram[i]
        if i < len(histogram) - 1:
            for j in range(i + 1, len(histogram), 1):

                if temp <= histogram[j]:
                    # print(temp_res)
                    temp_res += temp
                else:
                    break
        # if i > 0 and len(histogram) < 5:
        if i > 0:
            for k in range(i - 1, -1, -1):
                # print(temp_res)
                if temp <= histogram[k]:
                    # print(temp_res)
                    temp_res += temp
                else:
                    break

        if temp_res > res:
            res = temp_res
            temp_res = 0

    return res

#
print(largest_histogram([5]))
print(largest_histogram([5, 3]))
print(largest_histogram([1, 1, 4, 1]))
print(largest_histogram([1, 1, 3, 1]))
print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))
