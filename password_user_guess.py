""" asks for username and password to deduce who is tyrone """
correct_user = "Tyrone"
correct_pass = "1234"

guess_user = str(input("Username: "))
guess_pass = int(input("Password: "))

if guess_user == correct_user and guess_pass == correct_pass:
    print("Welcome, Tyrone.")
else:
    print("You are not Tyrone.")