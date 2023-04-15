students = []


class Student:
    students = ()

    def __init__(self, name, group, course, grades):
        self.name = name
        self.group = group
        self.course = course
        self.grades = grades
        students.append(self)

        print(f'+{name}')

    def add_grades(self, dir):
        self.grades = dir

    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def show_grades(self):
        return self.grades

    def show_group(self):
        return self.group


def average_grade_by_subject(subject):
    grades = []
    for i in students:
        grades.append(i.show_grades()[subject])
    return sum(grades) / len(grades)


def average_grade_by_group(group):
    grades = []
    for i in students:
        if i.show_group() == group:
            grades.append(i.average_grade())

    return sum(grades) / len(grades)


def average_grade_by_group_and_subject(group, subject):
    grades = []
    for i in students:
        if i.show_group() == group:
            grades.append(i.show_grades()[subject])
    return sum(grades) / len(grades)


grades1 = {'OOP': 5, 'Math': 5, 'English': 3, 'French': 5}
grades2 = {'PE': 3, 'Math': 3, 'English': 4, 'French': 3}
grades3 = {'OOP': 3, 'Math': 3, 'English': 5, 'French': 5}

Nemo = Student('Nemo', 234, 2, grades1)
Dori = Student('Dori', 234, 3, grades2)
Bob = Student('Bob', 230, 2, grades3)
print(f'Средний балл Nemo')
print(Nemo.average_grade())
print(f'Средний балл по математике')
print(average_grade_by_subject('Math'))
print(f'Средний балл в группе 234')
print(average_grade_by_group(234))
print(f'Средний балл по математике в группе 234')
print(average_grade_by_group_and_subject(234, 'English'))
