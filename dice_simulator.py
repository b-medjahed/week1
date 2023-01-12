choice= input("\nwould you like to roll a 1 to 6 die (y/n)? ") 

while True:
   while choice!="y" and choice!="n" :
      print("\nPlease make sure that you select the right option (y for yes or n for no).\n")
      choice= input("would you like to roll a 1 to 6 die (y/n)? ") 
   if choice=="y" :
      while choice=="y" :
            import random
            number=random.randint(1,6)
            print("\nYour result is: ", number)
            choice= input("\nwould like to roll again (y/n)? ")
   if choice=="n":
      print("\nSee you next time!\n")
      break