class Student:
    def __init__(self, first_name, last_name, age, avrg_point):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avrg_point = avrg_point

    def change_avrg_point(self, new_avrg_point):
        self.avrg_point = new_avrg_point

    def __str__(self):
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}, Середня оцінка: {self.avrg_point}"


student = Student("Yuriy", "Dmukhailo", 24, 95.9)
print(student)

student.change_avrg_point(100)
print(student)