from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disks, 0, -1):
  left_stack.push(i)
num_optimal_moves = pow(2, num_disks) - 1
print("\nThe fastest you can solve this game in {0} moves".format(num_optimal_moves))
#Set up the Game


#Get User Input, added 
def get_input():
  choices = [stack.get_name()[0].lower() for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter.upper(),name))
    user_input = input("").lower()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
    else: 
      print("Invalid input!")
#Play the Game
num_user_moves = 0
while (right_stack.get_size() != num_disks):
  print("\n\n\n...Current Stacks...")
  for stack in stacks: 
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if (from_stack.get_size() == 0):
      print("\n\nInvalid Move. Try again")
    elif (to_stack.get_size() == 0 or to_stack.peek() > from_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. try again")
  print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
