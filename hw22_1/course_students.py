from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from hw22_1.declarative_base import Base
import logging

logging.basicConfig(level=logging.INFO)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String, unique=True, nullable=False)
    is_active = Column(Integer, default=1)

    students = relationship("Student", back_populates="course")

    def __repr__(self):
        return f"id={self.id}, course_name='{self.course_name}'"



class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    is_active = Column(Integer, default=1)

    course = relationship("Course", back_populates="students")

    def __repr__(self):
        return f"course_id={self.id}, full_name='{self.full_name}', course_id={self.course_id}"
