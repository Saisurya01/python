movies=["bahubali","rrr","kgf","pushpa","vikram"]
print("My favorite movies are:")
for movie in movies:
    print(movie)
print(len(movies), "movies in the list.")
movies[0]=input("enter a new movie to add first in the list: ")
movies.append(input("enter a new movie to add in the list: "))
for movie in movies:
    print(movie)
print(len(movies), "movies in the list.")