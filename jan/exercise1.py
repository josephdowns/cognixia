# first_name, Last_name = input("What is your name? ").split()

name = input("What is your name? ")
age = input("What year were you born? ")

list = name.split()

first = list[0].capitalize()
last = list[1].capitalize()

digits = age[2:4]
# range is inclusive so [2:3] would exlude [3] but [2:4] includes [3]

email = first + "." + last + digits + "@company.com"

print(email)