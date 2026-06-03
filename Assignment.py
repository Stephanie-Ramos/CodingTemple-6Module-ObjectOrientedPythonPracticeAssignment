class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average_grade(self):
        if len(self.grades) == 0:
            return 0 
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Grades:", self.grades)
        

# Create 3 student objects with initial grades 
student1 = Student("Stephanie Johnson", "stephanie@example.com")
student1.add_grades = [88, 92]

student2 = Student("Marlene Brown", "marlene@example.com")
student2.grades = [80, 70]

student3 = Student("Logan Smith", "logan@example.com")
student3.grades = [95, 80]

# Add 2 new grades to each student
student1.add_grade(88)
student1.add_grade(98)

student2.add_grade(87)
student2.add_grade(73)

student3.add_grade(72)
student3.add_grade(85)

# Print information and average grade for each student
students = [student1, student2, student3]

for student in students:
    student.display_info
    print("Average Grade:", student.average_grade())

# Create a dictionary mapping email to Student object
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Function to safely retrieve a student by email 
def get_student_by_email(email):
    return student_dict.get(email)

# Example usage
student = get_student_by_email("stephanie@example.com")

if student:
    print("Student found:")
    student.display_info()
else:
    print("Student not found.")

# Create a set of all unique grades across all students
unique_grades = set()

for student in student_dict.values():
    unique_grades.update(student.grades)
    
#Print the set of unique grades
print("Unique Grades:", unique_grades)

