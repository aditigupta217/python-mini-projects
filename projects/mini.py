import random

print (" Welcome to the game , Guess the number")
target = random.randint(1,100)

while True:
   guess =  int(input(" Guess the number : "))
   if guess == target:
      print( " you guessed the corret number , you win !!!!")
      break 
   elif guess > target:
      print(" too high")
   else:
      print(" too low")

print (" Game over!!")      