# Set Boolean to true
keep_asking = True

#Start asking their name
while keep_asking == True:
    name = input("Enter your name")
    if name == "Ashton":
        keep_asking = false
    else:
        print("Wrong name")
        
# Loop is now finished, so greet Henry
print("Hi Ashton")