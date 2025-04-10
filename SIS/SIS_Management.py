from PYTHON.Student_Information_System.dao.Student_dao_impl import StudentDAOImpl
from PYTHON.Student_Information_System.dao.Course_dao_impl import CourseDAOImpl
from PYTHON.Student_Information_System.dao.Enrollment_dao_impl import EnrollmentDAOImpl
from PYTHON.Student_Information_System.dao.Payment_dao_impl import PaymentDAOImpl
from PYTHON.Student_Information_System.util.DBConnection import DBConnection
from PYTHON.Student_Information_System.dao.Teacher_dao_impl import TeacherDAOImpl
from PYTHON.Student_Information_System.dao.SIS_dao_impl import SISDAOImpl

from PYTHON.Student_Information_System.exception.CustomExceptions import StudentNotFoundException, CourseNotFoundException

class SISManagement:
    def __init__(self):
        self.conn = DBConnection.get_connection()
        print("Database connection established!")
        self.Student_dao = StudentDAOImpl()
        self.Course_dao = CourseDAOImpl()
        self.Enrollment_dao = EnrollmentDAOImpl()
        self.Payment_dao = PaymentDAOImpl()
        self.Teacher_dao = TeacherDAOImpl()
        self.SIS_dao = SISDAOImpl()

    ####Student Information
    def enrolll_in_course(self):
        self.Student_dao.enroll_in_course()
    def update_studnet_info(self):
        self.Student_dao.update_student_info()
    def add_student(self):
        self.Student_dao.add_student()
    def get_enrollments_for_student(self):
        self.Student_dao.get_enrolled_courses()
    def payment_history(self):
        self.Student_dao.get_payment_history()
    def make_payment(self):
        self.Student_dao.make_payment()
    def display_student_info(self):
        self.Student_dao.display_student_info()

    ####
    def get_all_courses(self):
        self.Course_dao.get_all_courses()
    def update_course_info(self):
        self.Course_dao.update_course_info()
    def display_course_info(self):
        self.Course_dao.display_course_info()
    def assign_course_to_teacher(self):
        self.Course_dao.assign_teacher()
    def get_courses_for_teacher(self):
        self.Course_dao.get_teacher()
    def caluclte_course_stastics(self):
        self.SIS_dao.calculate_course_statistics()

    ########
    def get_teacher_assigned_courses(self):
        self.Teacher_dao.get_assigned_courses()
    def update_teacher_info(self):
        self.Teacher_dao.update_teacher_info()
    def display_teacher_info(self):
        self.Teacher_dao.display_teacher_info()

    #####
    def add_enrollment(self):
        self.Enrollment_dao.add_enrollment()
    def view_all_enrollments(self):
        self.Enrollment_dao.get_all_enrollments()
    def student_enrollment(self):
        self.Enrollment_dao.get_student_by_enrollment()
    def course_enrollment(self):
        self.Enrollment_dao.get_course_by_enrollment()


    ##
    def add_payment(self):
        self.Payment_dao.add_payment()
    def get_payment_by_student(self):
        self.Payment_dao.get_student()
    def payment_amount(self):
        self.Payment_dao.get_payment_amount()
    def paymnet_dates(self):
        self.Payment_dao.get_payment_date()

    ###reports
    def enrollment_report(self):
        self.SIS_dao.generate_enrollment_report()
    def payment_report(self):
        self.SIS_dao.generate_payment_report()