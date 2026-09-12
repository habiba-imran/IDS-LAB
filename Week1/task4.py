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
