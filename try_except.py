
keep_asking = True

while keep_asking == True:
    try:
        value = int(input("Enter number: "))
        keep_asking = False
    except:
        print("That's not a number my bro!")
        
print("That's a cool number, bro, the number {}. I like the number {}.".format(value,value))