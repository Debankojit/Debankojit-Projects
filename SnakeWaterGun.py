import random


#The function to create a random guess/ the computer choice
def randomString():
  choices = ['snake','water','gun']
  computer = random.choice(choices)
  return computer
  
  
choices = ['snake','water','gun']
#The rules dict contains every winning condition of a match for the user
rules = {
    'snake':'water',
    'water':'gun',
    'gun':'snake'
  }
#The rules dict contains every drawing condition of a match for the user
rulesdraw = {
    'snake':'snake',
    'water':'water',
    'gun':'gun'
  }
point = 0
compPoint = 0
matches = int(input("Enter number of matches\n"))
if(matches<=0):  #Number of matches should always be more than ZERO
  print("matches cant be zero or negative")
#Looping for the number of matches
for i in range(matches):
  user = input("Enter your move: SNAKE  WATER  GUN\n")
  if(user not in choices):
    print("Invalid Choice")
    continue
  computerChoice = randomString()
  if rules[user]==computerChoice:
    print(computerChoice)
    print('You WIN, get 1 Point')
    point+=1
  elif rulesdraw[user]==computerChoice:
    print(computerChoice)
    print('Draw, No points')
  else:
    print(computerChoice)
    print('You loose, computer gets 1 point')
    compPoint+=1


print("You:  ", point )
print("Computer:   ", compPoint )




