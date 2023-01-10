import datetime
employees = []

def add_new_employee():
  first = input("First name: ")
  last = input("Last name: ")
  age = int(input("Age: "))
  email = f"{first}.{last}{str(datetime.date.today().year - age)[-2:]}@company.com"
  print("Employee added to database.")
  return {"first": first, "last": last, "email": email}
  # print(f"{first} {last} added to records with the email '{email}'")

while True:
  try:
    num = int(input("How many employees will you add? "))
    break
  except ValueError:
    print("Please enter an integer.")

while num > 0:
  # new_employee = add_new_employee()
  employees.append(add_new_employee())
  # import pdb; pdb.set_trace()
  num -= 1

print("")

for i in employees:
  # import pdb; pdb.set_trace()

  print(f"First name: {i['first']}")
  print(f"Surname: {i['last']}")
  print(f"Email: {i['email']}")
  print("-" * 10)

