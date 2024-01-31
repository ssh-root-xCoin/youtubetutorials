import random
print('I am thinking of a random number between 1 and 100! Can you guess it?')
number = random.randint(1, 101)
guessnumber = input("Enter guessed number by you: ")
attempts = 1
running = True
while running == True:
   if int(guessnumber) > 100 or int(guessnumber) < 1:
      print('Input not valid or allowed by this program due to what it was made for.')
   elif int(guessnumber) == number:
      print('You got it in {} attempts!'.format(attempts))
      running = False
      break
   elif int(guessnumber) > number:
      print('Guess lower!')
   elif int(guessnumber) < number:
      print('Guess higher!')

   attempts += 1
   guessnumber = input("Enter guessed number by you: ")
