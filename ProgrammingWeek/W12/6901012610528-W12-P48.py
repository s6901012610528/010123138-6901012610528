# code run in Thonny Python 3.14.4
# W12 : Example Classes
class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = float(weight)
        self.height = float(height)
        
    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Weight(kg) : {self.weight}")
        print(f"Height(m) : {self.height}")
        print(f"BMI : {self.getBMI():.2f}")
    
    def getBMI(self):
        BMI = self.weight/(self.height)**2
        return BMI

class Student(Person):
    def __init__(self, name, weight, height, student_id, gpa):
        super().__init__(name, weight, height)
        self.student_id = student_id
        self.gpa = float(gpa)
        
    def show_info(self):
        super().show_info()
        print(f"Student ID : {self.student_id}")
        print(f"GPA : {self.gpa}")
        
class Employee(Person):
    def __init__(self, name, weight, height, employee_id, salary):
        super().__init__(name, weight, height)
        self.employee_id = employee_id
        self.salary = salary
        
    def show_info(self):
        super().show_info()
        print(f"employee ID : {self.employee_id}")
        print(f"Salary : {self.salary}")
        
student1 = Student("AA", 75, 1.88, 6901012615599, 4.00)
employee1 = Employee("BB", 53, 1.68, 1122345, 100000)

student1.show_info()
print("------------")
employee1.show_info()