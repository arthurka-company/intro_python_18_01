# ООП - объектно-ориентированное программирование
# класс
# атрибут класса
# экземпляр (объект) класса
# метод класса

# __new__ -> __init__

import csv


class Student:
    def __init__(self, student_data):
        self.first_name = student_data.get('name')
        self.last_name = student_data.get('surname')
        self.age = student_data.get('age')
        self.marks = student_data.get('marks')

    def get_report_name(self):
        return f'{self.first_name[0].upper()}. {self.last_name}'

    def get_average_mark(self):
        if len(self.marks) > 0:
            return sum(self.marks.values()) / len(self.marks)
        return 0


class Group:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            self.students = []
        else:
            self.students = students

    def __len__(self):
        return len(self.students)

    def add_new_student(self, student):
        self.students.append(student)

    def get_students_count(self):
        return len(self.students)

    def get_average_mark(self):
        if len(self.students) > 0:
            return sum([student.get_average_mark() for student in self.students]) / len(self.students)
        return 0

    def get_simple_report(self):
        return [
            {'name': student.get_report_name(), 'average_mark': student.get_average_mark()}
            for student in self.students
        ]


if __name__ == '__main__':
    data = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'age': 23,
            'marks': {
                'math': 98,
                'english': 92
            }
        },
        {
            'name': 'Artur',
            'surname': 'Ivanov',
            'age': 33,
            'marks': {
                'math': 93,
                'english': 80
            }
        }
    ]
    group = Group('Our group 25')

    for student_info in data:
        student_obj = Student(student_info)
        print(student_obj.get_report_name())
        print(student_obj.get_average_mark())
        group.add_new_student(student_obj)

    print('Count:', group.get_students_count())
    print('Count:', len(group))
    print('Average mark:', group.get_average_mark())
    print(group.get_simple_report())

    with open(f'REPORT - {group.name}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'average_mark'])
        writer.writeheader()
        writer.writerows(group.get_simple_report())

