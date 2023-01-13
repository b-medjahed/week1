import random
my_number=random.randint(1,100)
print("\nAre you up for Guess The Number Challenge? You have 7 attempts only?\n")

choice=input("\nType in y for yes Or n for no: ")

while choice!="y" and choice!="n":
  choice=input("\nInvalid answer! Please type in y for yes Or n for no: ")

attempt=1


while True:
  
  if choice=="n":
   print("\nsee you next time!\n")
   break
  
  if attempt>7 :
    print("\nSorry! You have used up your seven attempts. ","The answer is ", my_number,"!\n")
    break
   
  user_number=input("\nPlease enter a number between 1 and 100: ")
  check=user_number
  try:
    check=int(user_number)
  except ValueError:
    print("Please enter a numerical value!")
    continue 

  if check==my_number:
     print("\nWell done. You guessed right!","You used ", attempt," attempt(s)\n")
     break
  if my_number>check:
     print("\nIncorrect guess. Your number is low!","You used ", attempt," attempt(s)")
     attempt+=1
  else:
     print("Incorrect guess. Your number is high!","You used ", attempt," attempt(s)")
     attempt+=1
