class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = sum(sum(grades_list) for grades_list in self.grades.values())
        total_count = sum(len(grades_list) for grades_list in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    # Добавление магических методов сравнения для класса Student
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_score(self):
        total_grades = sum(sum(grades_list) for grades_list in self.grades.values())
        total_count = sum(len(grades_list) for grades_list in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    # Добавление магических методов сравнения для класса Lecturer
    def __eq__(self, other):
        return self.average_score() == other.average_score()

    def __ne__(self, other):
        return self.average_score() != other.average_score()

    def __lt__(self, other):
        return self.average_score() < other.average_score()

    def __gt__(self, other):
        return self.average_score() > other.average_score()

    def __le__(self, other):
        return self.average_score() <= other.average_score()

    def __ge__(self, other):
        return self.average_score() >= other.average_score()


def calculate_average(entity_list, course):
    total_grades = sum(entity.average_grade() if isinstance(entity, Student) else entity.average_score()
                       for entity in entity_list if course in entity.grades)
    total_count = sum(1 for entity in entity_list if course in entity.grades)
    return total_grades / total_count if total_count != 0 else 0


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JAWA']

test_lecturer = Lecturer('Ivan', 'Petrovich')
test_lecturer.courses_attached += ['Python']

best_student.rate_hw(test_lecturer, 'Python', 7)

# Создание списка студентов и лекторов
students = [best_student]
lecturers = [test_lecturer]

# Вызов функций для расчета средней оценки студентов и лекторов
print("Средняя оценка студентов по курсу Python:", calculate_average(students, 'Python'))
print("Средняя оценка лекторов по курсу Python:", calculate_average(lecturers, 'Python'))
