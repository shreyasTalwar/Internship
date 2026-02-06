# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


# SportsPlayer class inherits from Person
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        Person.__init__(self, name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sport Name:", self.sport_name)


# CollegeStudent inherits from Student and SportsPlayer
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        print("College Name:", self.college_name)


# Creating object of CollegeStudent
cs = CollegeStudent(
    name="Shreyas",
    student_id=101,
    sport_name="Cricket",
    college_name="BGS Engineering College"
)

# Displaying all details
cs.display_person()
cs.display_student()
cs.display_sports_player()
cs.display_college_student()
