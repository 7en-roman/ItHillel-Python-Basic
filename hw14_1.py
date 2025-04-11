# ДЗ 14.1. Виняток користувача

class NumberOfStudentsError(Exception):
    def __init__(self, error_message= "You cannot add more than 10 students to the group!"):
        super().__init__(error_message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human: {self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender,age,first_name,last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, {self.gender}, {self.age} years old, {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise NumberOfStudentsError()

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number} \n{all_students} '


if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)

    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

    gr.delete_student('Taylor')
    print(gr)

    gr.delete_student('Taylor')
    print("-" * 100)

    try:
        for i in range(11):
            gr.add_student(Student('Male', 18 + i, f'Name{i}', f'Lastname{i}', f'RB{i}'))
    except NumberOfStudentsError as e:
        print(e)