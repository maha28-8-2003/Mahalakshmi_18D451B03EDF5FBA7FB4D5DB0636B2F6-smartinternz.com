class Student:
    def __init__(self, name, student_id, courses=None):
        self.name = name
        self.student_id = student_id
        self.courses = courses if courses is not None else []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_student_info(self):
        print(f"Student: {self.name}, ID: {self.student_id}")
        if self.courses:
            print("Courses enrolled: " + ", ".join(self.courses))
        else:
            print("No courses enrolled yet.")


# Example usage:
# Create students and enroll in courses
student1 = Student("John Doe", "S12345")
student2 = Student("Jane Smith", "S67890")

student1.enroll_course("Math")
student2.enroll_course("History")
student1.enroll_course("Math")  # Trying to enroll in the same course again

student1.display_student_info()
student2.display_student_info 