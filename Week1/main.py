# TASK # 02
name = "Habiba Imran"
print(name.upper(), "has", len(name), "characters")

# TASK # 03
weight = float(input("Enter your weight: "))
unit = input("Is your weight in kg or lbs? ")
if unit.lower() == "kg":
    lbs = weight * 2.20462
    print("Weight in lbs:", lbs)
elif unit.lower() == "lbs":
    kg = weight / 2.20462
    print("Weight in kg:", kg)
else:
    print("Invalid unit")

# TASK # 04
print("hello world!")
age = 20
print(f"The age is {age}")
name = "John"
age = 20
print(f"The name of patient is {name} and the age is {age}")
print(f"Hello Mr.{name}!")

integer_value = int(input("Enter an integer variable: "))
float_value = float(input("Enter float value: "))
print(f"The sum of {integer_value} and {float_value} is: {integer_value + float_value}")

str1 = "I am new in python"
print(str1.lower())
print(str1.upper())
str2 = str1.replace("new", "old")
print(str2)
location = str1.find("am")
print(location)

my_dict = {
    "names": ["habiba", "hadia", "zainab"],
    "age": [21, 22, 23],
    "city": ["rawalpindi", "islamabad", "rahim yar khan"]
}
print(my_dict["names"])
print(my_dict['city'][1])
print(my_dict["city"][0].upper())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

def add(num1, num2):
    return num1 + num2
result = add(5, 10)
print("The sum is:", result)

class Person:
    age = 10
    def greet(self):
        print("Hello, I am a person.")
harry = Person()
print(Person.greet)
print(harry.greet)
harry.greet()



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

# TASK # 06
class Employee:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
employee = Employee()
name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
salary = float(input("Enter employee salary: "))

employee.set_name(name)
employee.set_age(age)
employee.set_salary(salary)

print("\nEmployee Information")
print("Name:", employee.get_name())
print("Age:", employee.get_age())
print("Salary:", employee.get_salary())
