nom = (input("Entre ton nom: "))#note pour moi même ###001
age = int(input("Entre ton age: "))
genre = int(input("Entre 0 pour fille et 1 pour garçon:"))
#
if genre == 1:
    genre = "garçon"
elif genre == 0:
    genre = "fille"
elif genre >= 2:
    genre = "Null"

print("Id : " + nom + " " + str(age) + " " + str(genre))
