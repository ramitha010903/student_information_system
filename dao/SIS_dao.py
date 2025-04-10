
from abc import ABC, abstractmethod
from PYTHON.Student_Information_System.entity.Student import Student
from PYTHON.Student_Information_System.entity.Course import Course
from PYTHON.Student_Information_System.entity.Teacher import Teacher
from datetime import datetime

class SISDAO(ABC):

    @abstractmethod
    def enroll_student_in_course(self, student: Student, course: Course) -> bool:
        pass

    @abstractmethod
    def assign_teacher_to_course(self, teacher: Teacher, course: Course) -> bool:
        pass

    @abstractmethod
    def record_payment(self, student: Student, amount: float, payment_date: datetime) -> bool:
        pass

    @abstractmethod
    def generate_enrollment_report(self, course: Course):
        pass

    @abstractmethod
    def generate_payment_report(self, student: Student):
        pass

    @abstractmethod
    def calculate_course_statistics(self, course: Course):
        pass