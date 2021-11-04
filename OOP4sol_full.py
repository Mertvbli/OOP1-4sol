class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_student_grade(self):
        for i, v in self.grades.items():
            a = sum(v) / len(v)
            return f"{a:.1f}"

    def __str__(self):
        a = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_student_grade()}\n"
        b = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершённые курсы: Введение в программирование"
        return a + b

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.grades < other.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_lector_grade(self):
        for i, v in self.grades.items():
            a = sum(v) / len(v)
            return f"{a:.1f}"

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lector_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.grades < other.grades


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
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Nathan', 'Gimlik', 'Man')
best_student.courses_in_progress += ['Python', 'Git']
best_student.add_courses('Python')

second_student = Student('Hanna', 'Montana', 'Woman')
second_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(second_student, 'Python', 6)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 8)

cool_lecturer = Lecturer('Buddy', 'Holly')
cool_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Kollin', 'Farrell')
second_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 5)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student.rate_lecturer(second_lecturer, 'Python', 10)
best_student.rate_lecturer(second_lecturer, 'Python', 8)
best_student.rate_lecturer(second_lecturer, 'Python', 4)

best_lecturer = Student

print(second_student.courses_in_progress)
print(best_student.courses_in_progress)

print(cool_reviewer)

print(cool_lecturer)

print(best_student)

print(second_student.average_student_grade() < best_student.average_student_grade())

print(second_lecturer.average_lector_grade() > cool_lecturer.average_lector_grade())

student_list = [best_student, second_student]


def av_grade_all_st(student, subj):
    count = 0
    number = 0
    for i in student:
        for k, v in i.grades.items():
            if k == subj:
                count += sum(v)
                number += len(v)
    all = count / number
    return f"Средняя оценка всех студентов по курсу {subj} = {all:.1f}"


print(av_grade_all_st(student_list, 'Python'))

lecturer_list = [cool_lecturer, second_lecturer]


def av_grade_all_lec(lecturer, subj):
    count = 0
    number = 0
    for i in lecturer:
        for k, v in i.grades.items():
            if k == subj:
                count += sum(v)
                number += len(v)
    all = count / number
    return f"Средняя оценка всех лекторов по курсу {subj} = {all:.1f}"


print(av_grade_all_lec(lecturer_list, 'Python'))
