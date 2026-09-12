# TASK # 05
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
student1 = Student("Habiba", 20)
student1.display()
