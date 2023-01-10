class Employee:
  id_counter = 0
  
  def __init__(self, name, age, email, department):
    self.name = name
    self.age = age
    self.email = email
    self.department = department
    Employee.id_counter += 1

  def change_department(self, department):
    self.department = department

# joseph = Employee("Joseph", 34, "joseph.downs85@company.com", "Engineering")

# print(joseph.department)
# print("")
# import pdb; pdb.set_trace()
# joseph.change_department("Legal")
# print(joseph.department)