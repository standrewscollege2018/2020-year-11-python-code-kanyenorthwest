# this program calculates movie prices based off your age 
EIGHTEEN_PRICE = 12
THIRTEEN_PRICE = 9
SIX_PRICE = 7
FIVE_PRICE = 0

# asks for the age of the customer
age = int(input("What is your age sir? "))
if age >= EIGHTEEN_PRICE:
    print("Okey dokey your price is {} dollars my good man.".format(age * EIGHTEEN_PRICE))


