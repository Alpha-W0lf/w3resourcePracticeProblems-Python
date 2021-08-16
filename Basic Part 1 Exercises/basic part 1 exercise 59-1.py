# Write a Python program to convert height (in feet and inches) to centimeters.

given_height = input("Enter height in feet and inches (\' and \") : ")
given_list = given_height.split("\' ")
print(given_list)
given_ft = given_list[0]
given_in = given_list[1]

given_in = given_in.replace("\"","")
# inch to cm: multiply by 2.54

given_ft = int(given_ft)
given_in = int(given_in)

print(given_ft)
print(given_in)

ft_to_in = given_ft * 12
print(ft_to_in)

total_in = ft_to_in + given_in
print(total_in)

height_in_cm = total_in * 2.54
print(height_in_cm)