class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.attendance = {}

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def check_attendance(self):
        return self.attendance

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.roll_no] = student

    def mark_attendance(self, roll_no, date, status):
        student = self.students.get(roll_no)
        if student:
            student.mark_attendance(date, status)

    def check_attendance(self, roll_no):
        student = self.students.get(roll_no)
        if student:
            return student.check_attendance()
        else:
            return "Student not found."

# Initialize the system and add some students
attendance_system = AttendanceSystem()
student1 = Student("Aung Aung", "2")
student2 = Student("Mg Mg", "7")
attendance_system.add_student(student1)
attendance_system.add_student(student2)

# Mark attendance for some students
attendance_system.mark_attendance("2", "2022-01-01", "Present")
attendance_system.mark_attendance("7", "2022-01-01", "Present")

# Check attendance for a student
print(attendance_system.check_attendance("2"))
print(attendance_system.check_attendance("7"))
