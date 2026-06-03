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

# Example Usage
# student1 = Student("Stephanie Johnson", "stephanie@example.com")
# student1.add_grade(90)
# student1.add_grade(85)
# student1.add_grade(95)
# student1.display_info()
# print("Average Grade:", student1.average_grade())

        