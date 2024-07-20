'''
user input example.
create a program that asks the user to enter their name and age.
prints name, age, and when teh user will turn 100 years old.
'''

name = input("Give me your name:")
age = input("Give me your age:")
age = int(age)
hundred_years = 2024 + (100 - age)

print("You are", name, str(age), "years old")
print("You will turn 100 years old in", str(hundred_years))