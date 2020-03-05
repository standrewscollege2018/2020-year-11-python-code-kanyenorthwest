place_in_favourites = []
NUMBER_OF_FAVOURITES = 5

print("Your favourite movies are")

for i in range(NUMBER_OF_FAVOURITES) :
    
    name = input("Enter favourite movie: ")
    place_in_favourites.append(name)
    
print(place_in_favourites)