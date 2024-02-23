import random

number = random.randrange(1,35)
guess = int(input("Guess a number between 1 and 35: "))

while guess != number:
   if guess < number:
       print("Too Low! Guess a higher number!")
       guess = int(input("\nGuess a number between 1 and 35: "))
   else:
        print("Too High! Guess a Lower number!")
        guess = int(input("\nGuess a number between 1 and 35: "))

print("You guessed the number correctly!")
