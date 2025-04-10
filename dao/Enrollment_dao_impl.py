import pyodbc
from PYTHON.Student_Information_System.dao.Enrollment_dao import IEnrollmentDAO
from PYTHON.Student_Information_System.util.DBConnection import DBConnection

class EnrollmentDAOImpl(IEnrollmentDAO):
    def get_student_by_enrollment(self) -> None:
        try:
            enrollment_id = int(input("Enter Enrollment ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT s.student_id, s.first_name, s.last_name, s.email
                FROM edu.Enrollments e
                JOIN edu.Students s ON e.student_id = s.student_id
                WHERE e.enrollment_id = ?
            """
            cursor.execute(query, (enrollment_id,))
            result = cursor.fetchone()

            if result:
                print("\nStudent Information:")
                print(f"ID: {result.student_id}")
                print(f"Name: {result.first_name} {result.last_name}")
                print(f"Email: {result.email}")
            else:
                print("No student found for the given enrollment ID.")
        except Exception as e:
            print("Error retrieving student:", e)

    def get_course_by_enrollment(self) -> None:
        try:
            enrollment_id = int(input("Enter Enrollment ID to get associated course: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT c.course_id,  c.course_name
                FROM edu.Enrollments e
                JOIN edu.Courses c ON e.course_id = c.course_id
                WHERE e.enrollment_id = ?
            """
            cursor.execute(query, (enrollment_id,))
            result = cursor.fetchone()

            if result:
                print("\nCourse Information:")
                print(f"Course Name: {result.course_name}")
            else:
                print("No course found for the given enrollment ID.")
        except Exception as e:
            print("Error retrieving course:", e)

    def add_enrollment(self):
        try:
            student_id = int(input("Enter student ID: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()


            cursor.execute("SELECT COUNT(*) FROM edu.Students WHERE student_id = ?", (student_id,))
            if cursor.fetchone()[0] == 0:
                print(" Student not found.")
                return


            course_id = int(input("Enter course ID: "))
            cursor.execute("SELECT COUNT(*) FROM edu.Courses WHERE course_id = ?", (course_id,))
            if cursor.fetchone()[0] == 0:
                print("Course not found.")
                return

            # Check for duplicate enrollment
            cursor.execute("SELECT COUNT(*) FROM edu.Enrollments WHERE student_id = ? AND course_id = ?",
                           (student_id, course_id))
            if cursor.fetchone()[0] > 0:
                print("Student is already enrolled in this course.")
                return

            # Insert enrollment
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            cursor.execute("INSERT INTO edu.Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
                           (student_id, course_id, enrollment_date))
            conn.commit()
            print("Enrollment added successfully.")

        except Exception as e:
            print(f"Error while adding enrollment: {e}")

    def get_all_enrollments(self):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
            SELECT 
                e.enrollment_id,
                s.student_id,
                s.first_name,
                s.last_name,
                c.course_id,
                c.course_name,
                e.enrollment_date
            FROM edu.Enrollments e
            JOIN edu.Students s ON e.student_id = s.student_id
            JOIN edu.Courses c ON e.course_id = c.course_id
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                print(" No enrollments found.")
            else:
                print("All Enrollments:")
                for row in rows:
                    print(
                        f"Enrollment ID: {row[0]} | Student: {row[2]} {row[3]} (ID: {row[1]}) | Course: {row[5]} (ID: {row[4]}) | Date: {row[6]}")
            return rows

        except Exception as e:
            print(f"Error fetching enrollments: {e}")
            return []
