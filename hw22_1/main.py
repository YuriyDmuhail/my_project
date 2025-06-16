import logging

from requests import Session

from hw22_1.course_students import Course, Student
from hw22_1.declarative_base import Base
from hw22_1.bd_client import SQLAlchemyClient
import random
from hw22_1.random_full_name import get_user, get_int_to_20


client = SQLAlchemyClient()
session = client.get_session()

# створення курсів
courses = session.query(Course).all()

if not courses:
    course_names = ["Python", "Data Science", "SQL"]
    for name in course_names:
        session.add(Course(course_name=name))
    session.commit()
    courses = session.query(Course).all()

# створення студентів
for i in range(6):
    full_name = get_user()
    course = random.choice(courses)
    student = Student(full_name=full_name, course=course)
    session.add(student)
session.commit()

def get_students_by_course(course_name: str, session):
    course = session.query(Course).filter(Course.course_name == course_name).first()
    if course:
        return course.students
    return []



def update_course_name(course_id: int, new_name: str, session):
    course = session.query(Course).filter(Course.id == course_id).first()
    if course:
        course.course_name = new_name
        session.commit()
        logging.info(f"Назву курсу оновлено на {new_name}")
    else:
        logging.info("Курс не знайдено.")

def update_student_name(student_id: int, new_name: str, session):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.full_name = new_name
        session.commit()
        logging.info(f"Ім'я студента - '{student.full_name}' оновлено на - '{new_name}'")
    else:
        logging.info(f"Студента не знайдено.")



def deactive_student(student_id: int, session):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.is_active = 0
        session.commit()
        logging.info(f"Студента '{student.full_name}' (id={student.id}) деактивовано.")
    else:
        logging.info(f"Студента '{student.full_name}' не знайдено.")


#Шукаємо студентів на якомусь курсі
students = get_students_by_course("Python Basics", session)
print(students)

#Деактивація студента
studentid= get_int_to_20()
print(studentid)
deact_student = deactive_student(studentid, session)

#апдейт ім'я студента
new_name = get_user()
updated_student_name = update_student_name(studentid, new_name, session)

#апдейт назви курсу
new_course_name = update_course_name(1, "Python Basics", session)

