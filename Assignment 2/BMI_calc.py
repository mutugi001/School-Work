#Collins Mutugi Wachira
#SCT211-0051/2022

import math
height = float(input("enter your height(m): "))
weight = float(input("enter your weight(kg): "))
height_squared = height * height
BMI = round(weight/height_squared, 1)
print(BMI)

if BMI < 18.5:
    print("underweight")
elif BMI <= 24.9:
    print("normal weight")
elif BMI <= 29.9:
    print("overweight")
else:
    print("overweight")