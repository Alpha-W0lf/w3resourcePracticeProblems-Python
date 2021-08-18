# Write a Python program to calculate body mass index.

# BMI formula: (weight / ((height) ** 2)) * 703

weight = float(input("Enter your weight in pounds: "))
height = input("Enter your height in feet and inches using (\' \") format: ")

height_list = height.split("' ")
height_list[1] = height_list[1].replace("\"","")

height_list_int = list(map(int, height_list))

print(height_list_int)
height_inches = (height_list_int[0] * 12) + height_list_int[1]
print(height_inches)

BMI = (weight / ((height_inches) ** 2) * 703)

print("BMI is:", BMI)