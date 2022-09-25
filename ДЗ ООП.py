class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
            n = 0
            grade = 0
            for i in self.grades.values():
                for j in i:
                    n += 1
                    grade += j
            return grade/n

    def __str__(self):
        return f'Имя: {self.name}\n' \
                f'Фамилия: {self.surname}\n' \
                f'Средняя оценка за лекции: {self.average_rating()}\n'\
                f'Курсы в процесе изучения: {", ".join(self.courses_in_progress)}\n' \
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() > other.average_rating()

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        n = 1
        grade = 0
        for i in self.grades.values():
            for j in i:
                n = 0
                n += 1
                grade += j
        return grade/n

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating()}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() > other.average_rating()


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Виктор', 'Семёнов', 'муж')
student1.courses_in_progress += ['Python Pro']
student1.finished_courses += ['SQL']
student1.finished_courses += ['Python']
student1.courses_in_progress += ['Java']
student1.grades = {'Python': [10, 10, 10], 'SQL': [7, 7, 7]}

student2 = Student('Максим', 'Волков', 'муж')
student2.courses_in_progress += ['Python Pro']
student2.finished_courses += ['SQL']
student2.finished_courses += ['Python']
student2.courses_in_progress += ['Java']
student2.grades = {'Python': [8, 8, 8], 'SQL': [7, 7, 7]}

mentor1 = Lecturer('Светлана', 'Тонкова')
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['Java']

mentor2 = Lecturer('Олег', 'Кочевой')
mentor2.courses_attached += ['Python Pro']
mentor2.courses_attached += ['SQL']

mentor3 = Reviewer('Анастасия', 'Галицина')
mentor3.courses_attached += ['Python']
mentor3.courses_attached += ['Java']

mentor4 = Reviewer('Сергей', 'Круг')
mentor4.courses_attached += ['Python Pro']
mentor4.courses_attached += ['SQL']

mentor3.rate_hw(student1, 'Python', 10)
mentor3.rate_hw(student1, 'Python', 10)
mentor3.rate_hw(student1, 'Python', 10)

mentor3.rate_hw(student1, 'Java', 9)
mentor3.rate_hw(student1, 'Java', 9)
mentor3.rate_hw(student1, 'Java', 9)

mentor3.rate_hw(student2, 'Python', 8)
mentor3.rate_hw(student2, 'Python', 8)
mentor3.rate_hw(student2, 'Python', 8)

mentor3.rate_hw(student2, 'Java', 8)
mentor3.rate_hw(student2, 'Java', 8)
mentor3.rate_hw(student2, 'Java', 8)

mentor4.rate_hw(student1, 'Python Pro', 5)
mentor4.rate_hw(student1, 'Python Pro', 5)
mentor4.rate_hw(student1, 'Python Pro', 6)

mentor4.rate_hw(student1, 'SQL', 7)
mentor4.rate_hw(student1, 'SQL', 7)
mentor4.rate_hw(student1, 'SQL', 7)

mentor4.rate_hw(student2, 'Python Pro', 8)
mentor4.rate_hw(student2, 'Python Pro', 8)
mentor4.rate_hw(student2, 'Python Pro', 8)

mentor4.rate_hw(student2, 'SQL', 8)
mentor4.rate_hw(student2, 'SQL', 8)
mentor4.rate_hw(student2, 'SQL', 8)


student1.rate_lc(mentor1, 'Python', 7)
student1.rate_lc(mentor1, 'Python', 7)
student1.rate_lc(mentor1, 'Python', 7)

student2.rate_lc(mentor1, 'Java', 9)
student2.rate_lc(mentor1, 'Java', 9)
student2.rate_lc(mentor1, 'Java', 5)

student1.rate_lc(mentor2, 'Python Pro', 7)
student1.rate_lc(mentor2, 'Python Pro', 7)
student1.rate_lc(mentor2, 'Python Pro', 7)

student2.rate_lc(mentor2, 'SQL', 7)
student2.rate_lc(mentor2, 'SQL', 7)
student2.rate_lc(mentor2, 'SQL', 7)

# print(student1.grades)
# print(student2.grades)

# print(mentor1.grades)
# print(mentor2.grades)

# print(student1)
# print(student2)

# print(mentor1)
# print(mentor2)

# print(student1.__lt__(student2))
# print(mentor1.__lt__(mentor2))

student_list = [student1, student2]


def average_rating_course_student (student_list, course):
    for student in student_list:
        print (student.name)
        n = 0
        sum = 0
        for i in student.grades[course]:
            sum +=i
            n +=1
        print (sum/n)

lecturer_list = [mentor1, mentor2]

def average_rating_course_lecturer (lecturer_list, course):
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            print (lecturer.name)
            n = 0
            sum = 0
            for i in lecturer.grades[course]:
                sum +=i
                n +=1
            print (sum/n)


average_rating_course_student(student_list, 'Python')    
average_rating_course_lecturer (lecturer_list, 'SQL')