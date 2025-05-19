# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.department = programming_language

# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

#lead = TeamLead("Sara", 25, "IT", "Python", 3)

def test_attributes():
    lead = TeamLead("Oksana", 5000, "IT", "Python", 4)

    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead, "team_size")