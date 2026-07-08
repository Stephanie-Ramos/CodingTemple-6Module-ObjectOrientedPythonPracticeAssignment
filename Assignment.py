# Part 1: Class Definition 
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

# Part 4: add grades_tuple() menthod to my Student class
    def grades_tuple(self):
        return tuple(self.grades)
        
# Part 2: Working with Objects 
# Create 3 student objects with initial grades 
student1 = Student("Stephanie Johnson", "stephanie@example.com")
student1.grades = [88, 92]

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
    student.display_info()
    print("Average Grade:", student.average_grade())

# Part 3: Dictionary and Set Integration
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

# Part 4: Tuple Practice 
# Get grades as a tuple 
grades = student1.grades_tuple()
print("Grades Tuple:", grades)

# Try to modify the tuple
try:
    grades[0] = 100
except TypeError as e:
    print("Tuples are immutable and cannot be changed.")
    print("Error:", e)
    
# Part 5: List Operations 
# Remove the last grade from each student's grade list 
for student in students:
    removed_grade = student.grades.pop()
    print(f"Removed grade {removed_grade} from {student.name}")

print("\nUpdated Student Information:")

# Access and print the first and last grade
for student in students:
    print(f"\nStudent: {student.name}")
    print("Grades:", student.grades)
    
    if len(student.grades) > 0:
        print("First Grade:", student.grades[0])
        print("Last Grade:", student.grades[-1])
        
        # Print the number of grades
        print("Number of Grades:", len(student.grades))
        
# Part 6: Bonus
import re 

# Regular expression pattern for name@domain.com
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$'

# Validate student emails
print("Email Validation Results:")
for student in students:
    if re.match(email_pattern, student.email):
        print(f"{student.email} is a valid email.")
    else:
        print(f"{student.email} is NOT a valid email")

# Count grades above 90 across all students
count_above_90 = 0 

for student in students:
    for grade in student.grades:
        if grade > 90:
            count_above_90 += 1

print("\nNumber of grades above 90:", count_above_90)

        