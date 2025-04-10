# DuplicateEnrollmentException: Thrown when a student is already enrolled in a course.
class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in the course."):
        super().__init__(message)

# CourseNotFoundException: Thrown when a course does not exist in the system.
class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found."):
        super().__init__(message)

# StudentNotFoundException: Thrown when a student does not exist in the system.
class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found."):
        super().__init__(message)

# TeacherNotFoundException: Thrown when a teacher does not exist in the system.
class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found."):
        super().__init__(message)

# PaymentValidationException: Thrown when there is an issue with payment validation.
class PaymentValidationException(Exception):
    def __init__(self, message="Payment validation failed."):
        super().__init__(message)

# InvalidStudentDataException: Thrown when provided data for student is invalid.
class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data provided."):
        super().__init__(message)

# InvalidCourseDataException: Thrown when provided data for course is invalid.
class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data provided."):
        super().__init__(message)

# InvalidEnrollmentDataException: Thrown when provided data for enrollment is invalid.
class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data provided."):
        super().__init__(message)

# InvalidTeacherDataException: Thrown when provided data for teacher is invalid.
class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data provided."):
        super().__init__(message)

# InsufficientFundsException: Thrown when a student doesn't have enough funds for payment.
class InsufficientFundsException(Exception):
    def __init__(self, message="Student does not have sufficient funds to make the payment."):
        super().__init__(message)


