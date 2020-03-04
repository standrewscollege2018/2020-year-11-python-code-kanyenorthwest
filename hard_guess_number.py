# correct_number
from random import randrange
Num = randrange(1,101)
keep_asking = True

while keep_asking == True:
    guess = int(input("Guess the number: "))
    if guess < Num:
        print("Too low budza.")
    elif guess > Num:
        print("Too high budza!")
    elif guess == Num:
        keep_asking == False
        
# Loop is done, congratulate them
print("Yo! You got it right!")