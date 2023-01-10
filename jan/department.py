class Department:
  department_counter = 0

  def __init__(self, name, employee_count):
    self.name = name
    self.employee_count = employee_count
    Department.department_counter += 1

  def add_employees(self, number):
    self.employee_count += number
  
  def subtract_employees(self, number):
    self.employee_count -= number


marketing = Department("Marketing", 6)

import pdb; pdb.set_trace()