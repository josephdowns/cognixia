# print("Player1, please input r, s, or p. ")
# play1 = input()

#  import pdb; pdb.set_trace()

# if play1 != 'r' or 's' or 'p':
#   print("Input not recognized. Please re-enter. ")
#   play1 = input()

# print("Player2, please input r, s, or p. ")
# play2 = input()

# if play2 != 'r' or 's' or 'p':
#   print("Input not recognized. Please re-enter. ")
#   play2 = input()

# if play1 == "r":
#   if play2 == "r":
#     print("Draw!")
#   elif play2 == "s":
#     print("Player1 wins!")
#   else:
#     print("Player2 wins!")

# if play1 == "s":
#   if play2 == "s":
#     print("Draw!")
#   elif play2 == "p":
#     print("Player1 wins!")
#   else:
#     print("Player2 wins!")

# if play1 == "p":
#   if play2 == "p":
#     print("Draw!")
#   elif play2 == "r":
#     print("Player1 wins!")
#   else:
#     print("Player2 wins!")
print("Welcome to Rock, Paper, Scissors! Please enter r, p, s.")

while True:
  p1 = input("Player 1: ")

# if (p1 != 'r') or (p1 != 's') or (p1 != 'p'):
  if p1 not in ('r', 'p', 's'):
    print("Please enter r, p, or s.")
  else:
    break

while True:
  p2 = input("Player 2: ")
  if p2 not in ('r', 'p', 's'):
    print("Please enter r, p, or s.")
  else:
    break

if (p1 == p2):
  print("Draw")
elif (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")