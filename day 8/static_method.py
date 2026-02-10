class Student:
    # Class Variable (shared by all students)
    college_name = "ABC College"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-------------------")

    # Classmethod
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Staticmethod
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


# 🔹 Main Program

# Create 2 students
s1 = Student("Ravi", 101)
s2 = Student("Anita", 102)

# Print student details
s1.display()
s2.display()

# Change college name using classmethod
Student.change_college("XYZ Engineering College")

# Print again (college name updated for both)
s1.display()
s2.display()

# Use staticmethod
print("Ravi Result:", Student.is_pass(78))
print("Anita Result:", Student.is_pass(30))
