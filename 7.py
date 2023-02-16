print("Первое задание")

x = 235


def reverse_num(x):
    res = 0
    print(f"Число:{x}")
    while x > 0:
        res = (res * 10) + x % 10
        x //= 10
    return res


print(reverse_num(x))

print("Второе задание")

word = 'топот'


def is_pal(word):
    for k in range(len(word)):
        if word[k] != word[len(word) - k - 1]:
            return False
    return True


print(word, '=', is_pal(word))

print("Третье задание")

student1 = {'Name': 'Vladislav', 'Surname': 'Romantsov', 'Patronymic': 'Igorevich', 'Date_birth': 2002, 'Course': 3,
            'Group_number': "430-4", 'Marks': {'OOP': 5, 'Math': 5, 'English': 3, 'French': 5}}
student2 = {'Name': 'Igor', 'Surname': 'Lugovskoy', 'Patronymic': 'Romanovich', 'Date_birth': 2000, 'Course': 4,
            'Group_number': "429-2", 'Marks': {'PE': 3, 'Math': 3, 'English': 4, 'French': 3}}
student3 = {'Name': 'Kirill', 'Surname': 'Kashin', 'Patronymic': 'Romanovich', 'Date_birth': 2003, 'Course': 3,
            'Group_number': "430-4", 'Marks': {'OOP': 3, 'Math': 3, 'English': 5, 'French': 5}}
students = [student1, student2, student3]


def studentList(students, Course):
    res = []
    for i in range(len(students)):
        if students[i]['Course'] == Course:
            res.append(students[i]['Surname'] + ' ' + students[i]['Name'] + ' ' + students[i]['Patronymic'])
    res.sort()
    return (res)


print('3 course students:', studentList(students, 3))


def midMark(students, Group_number):
    res = {}
    arrmarks = [0, 0, 0, 0]
    summ = 0
    k = 0
    for i in range(len(students)):
        if students[i]['Group_number'] == Group_number:
            res = students[i]['Marks']
            summ += 1
            for mark in students[i]['Marks']:
                arrmarks[k] += students[i]['Marks'][mark]
                k += 1
        k = 0
        i = 0

    for mark in res:
        res[mark] = arrmarks[i] / summ
        i += 1

    return res


Group_number = '430-4'
print("Average mark of", Group_number, midMark(students, Group_number))


def minmax(students):
    res_min = students[0]["Date_birth"]
    res_max = students[0]["Date_birth"]
    res_index_max = 0
    res_index_min = 0
    for i in range(len(students)):
        if students[i]['Date_birth'] > res_min:
            res_min = students[i]['Date_birth']
            res_index_max = i
        if students[i]['Date_birth'] < res_max:
            res_min = students[i]['Date_birth']
            res_index_min = i
    print('Youngest student:', students[res_index_max]['Surname'] + ' ' + students[res_index_max]['Name'])
    print('Older student:', students[res_index_min]['Surname'] + ' ' + students[res_index_min]['Name'])
    return res_index_max, res_index_min


minmax(students)


def calcmid(dct):  # считаем средния балл студента
    sm = 0
    for i in dct:
        sm += dct[i]
    return sm / len(dct)


def best_students(students):
    groups = []
    tmax = 0
    for i in range(len(students)):
        if students[i]['Group_number'] not in groups:
            groups.append(students[i]['Group_number'])
    for k in range(len(groups)):
        for i in range(len(students)):

            if students[i]['Group_number'] == groups[k] and tmax < calcmid(students[i]['Marks']):
                tmax = calcmid(students[i]['Marks'])
                idsest = i
        print("Best student", groups[k], students[idsest]['Surname'], students[idsest]['Name'])
        tmax = 0


best_students(students)
