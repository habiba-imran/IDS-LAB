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
