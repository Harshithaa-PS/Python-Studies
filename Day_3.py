vijay = ["Gilli","Master","Pokiri","Shajahan","Leo","Sarkar","Jilla","Badhiri","Nanban","Kushi"]
suriya = ["Karuppu","Kaka kaka","Friends","Vel","Anjaan","Ayan","Ghajini","Singham","Mass","Jai Bhim"]
karthi = ["Siruthai","Paiya","Thozha","Viruman","Dev","Paruthiveeran","Madras","Kashmora","Sulthan","Meiyazhagan"]

def show_movies(movies, count):
    for i in range(min(count, len(movies))):
        print(i + 1, movies[i])

choice = int(input("Please enter top x number (maximum 10): "))
actor = input("Enter the actor name (vijay, suriya, karthi): ").lower()

if actor == "vijay":
    show_movies(vijay, choice)
elif actor == "suriya":
    show_movies(suriya, choice)
elif actor == "karthi":
    show_movies(karthi, choice)
else:
    print("Actor not found")
