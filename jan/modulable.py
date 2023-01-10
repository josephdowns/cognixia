def get_num():
  while True:
    try:
      num = int(input("Please enter a number: "))
      break
    except ValueError:
      print("Please enter an integer.")  
  print(f"You entered {num}")
  return num