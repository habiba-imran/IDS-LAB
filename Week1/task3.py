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
