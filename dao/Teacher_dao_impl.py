from PYTHON.Student_Information_System.dao.Teacher_dao import ITeacherDAO
from  PYTHON.Student_Information_System.util.DBConnection import DBConnection


class TeacherDAOImpl(ITeacherDAO):

    def update_teacher_info(self) -> bool:
        try:
            teacher_id = int(input("Enter the Teacher ID to update: "))

            print("\nWhich field do you want to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Email")
            print("4. Expertise")
            choice = input("Enter your choice (1-4): ")

            field_map = {
                '1': 'first_name',
                '2': 'last_name',
                '3': 'email',
                '4': 'expertise'
            }

            if choice not in field_map:
                print("Invalid choice.")
                return False

            new_value = input(f"Enter new value for {field_map[choice]}: ")

            query = f"UPDATE edu.Teacher SET {field_map[choice]} = ? WHERE teacher_id = ?"

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (new_value, teacher_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("Teacher information updated successfully.")
                return True
            else:
                print("No teacher found with the given ID.")
                return False

        except Exception as e:
            print("Error updating teacher info:", e)
            return False

    def display_teacher_info(self) -> None:
        try:
            teacher_id = int(input("Enter Teacher ID to view info: "))

            query = "SELECT * FROM edu.Teacher WHERE teacher_id = ?"
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (teacher_id,))
            row = cursor.fetchone()

            if row:
                print("\n--- Teacher Information ---")
                print(f"ID       : {row.teacher_id}")
                print(f"Name     : {row.first_name}{row.last_name}")
                print(f"Email    : {row.email}")

            else:
                print("No teacher found with the given ID.")

        except Exception as e:
            print("Error fetching teacher info:", e)


    def get_assigned_courses(self) -> None:
        try:
            teacher_id = int(input("Enter Teacher ID to view assigned courses: "))

            query = """
            SELECT course_id, course_name 
            FROM edu.Courses 
            WHERE teacher_id = ?
            """
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (teacher_id,))
            rows = cursor.fetchall()

            print("\n--- Assigned Courses ---")
            if rows:
                for row in rows:
                    print(f"Course ID: {row.course_id} | Name: {row.course_name}")
            else:
                print("No courses assigned to this teacher.")

        except Exception as e:
            print("Error fetching assigned courses:", e)

    def assign_course_to_teacher(self):
        try:
            teacher_id = int(input("Enter teacher ID: "))
            course_id = int(input("Enter course ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Validate teacher
            cursor.execute("SELECT COUNT(*) FROM edu.Teacher WHERE teacher_id = ?", (teacher_id,))
            if cursor.fetchone()[0] == 0:
                print("Teacher not found.")
                return

            # Validate course
            cursor.execute("SELECT COUNT(*) FROM edu.Courses WHERE course_id = ?", (course_id,))
            if cursor.fetchone()[0] == 0:
                print("Course not found.")
                return

            # Assign teacher
            cursor.execute("UPDATE edu.Courses SET teacher_id = ? WHERE course_id = ?", (teacher_id, course_id))
            conn.commit()

            print("Course successfully assigned to teacher.")

        except Exception as e:
            print(f"Error assigning course to teacher: {e}")