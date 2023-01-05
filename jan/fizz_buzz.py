answer = input("Please enter a number: ")

number = int(answer)

fizz = 0
buzz = 0
fizzbuzz = 0
sum = 0

# import pdb; pdb.set_trace()

for i in range(1, number+1):
  sum += i
  if (i % 3 == 0) and (i % 5 == 0):
    print("Fizzbuzz")
    fizzbuzz += 1
  elif i % 3 == 0:
    print("Fizz")
    fizz += 1
  elif i % 5 == 0:
    print("Buzz")
    buzz +=1
  else:
    print(i)

print(f"Sum of integers: {sum}")
print(f"Count of Fizzes: {fizz}")
print(f"Count of Buzzes: {buzz}")
print(f"Count of Fizzbuzzes: {fizzbuzz}")