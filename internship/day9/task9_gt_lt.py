class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary > other.salary

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary < other.salary


e1 = Employee("Asha", 60000)
e2 = Employee("Ravi", 50000)

print(e1 > e2)
print(e1 < e2)
