class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        self.average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                  f'{self.average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result

    def __lt__(self, other):
        self.average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        other.average_grade = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))
        if isinstance(other, Student):
            return self.average_grade < other.average_grade
        else:
            print('Данные введены не верно')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        self.average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return result

    def __lt__(self, other):
        self.average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        other.average_grade = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade
        else:
            print('Данные введены не верно')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


def average_grade_students(list_students, course):
    average_students_grade = (sum([sum(student.grades[course]) for student in list_students]) /
                              sum([len(student.grades[course]) for student in list_students]))
    to_print = f'Средняя оценка за домашние задания на курсе {course}: {average_students_grade}'
    print(to_print)


def average_grade_lecturers(list_lecturers, course):
    average_lecturers_grade = (sum([sum(lecturer.grades[course]) for lecturer in list_lecturers]) /
                               sum([len(lecturer.grades[course]) for lecturer in list_lecturers]))
    to_print = f'Средняя оценка за лекции на курсе {course}: {average_lecturers_grade}'
    print(to_print)


first_student = Student('Ivan', 'Ivanov', 'man')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['GIT']
first_student.courses_in_progress += ['Введение в программирование']
second_student = Student('Petr', 'Petrov', 'man')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['GIT']

first_reviewer = Reviewer('Neto', 'Logy')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Homework', 'Checker')
second_reviewer.courses_attached += ['Python', 'GIT']


first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 7)
second_reviewer.rate_hw(first_student, 'Python', 2)
second_reviewer.rate_hw(first_student, 'Python', 9)

first_reviewer.rate_hw(second_student, 'Python', 3)
first_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'Python', 2)
second_reviewer.rate_hw(second_student, 'Python', 10)

first_lecturer = Lecturer('Alexey', 'Smirnov')
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Igor', 'Pavlov')
second_lecturer.courses_attached += ['Python', 'GIT']


first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 8)
second_student.rate_lecturer(first_lecturer, 'Python', 6)
second_student.rate_lecturer(first_lecturer, 'Python', 7)

first_student.add_finished_courses('Введение в программирование')

first_student.rate_lecturer(second_lecturer, 'Python', 5)
first_student.rate_lecturer(second_lecturer, 'Python', 7)
second_student.rate_lecturer(second_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 9)

second_student.add_finished_courses('Введение в программирование')
#
average_grade_students([first_student, second_student], 'Python')
average_grade_lecturers([first_lecturer, second_lecturer], 'Python')

print()
print('Студенты:')
print(first_student)
print(second_student)
print()
print('Проверяющие:')
print(first_reviewer)
print(second_reviewer)
print()
print('Лекторы:')
print(first_lecturer)
print(second_lecturer)
print()
print('Сравнение студентов:')
print(first_student < second_student)
print()
print('Сравнение лекторов:')
print(first_lecturer < second_lecturer)
