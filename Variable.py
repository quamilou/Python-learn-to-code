#type String

nom = "Saenz"
prenom = "Quentin"
nomprenom = nom + prenom
#Attention ne pas oublier les ""
print("1-Bonjour "+ prenom)
#Tu peux verifier le type d'une variable avec :
print(type(prenom))


#type Integer

age = 23
age2 = 19+1
age3 = age2 + 1
#Attention ne pas oublier str() pour les variable qui ne sont pas de type String
print("2-"+prenom+" a "+str(age2)+" ans.")
#Tu peux verifier le type d'une variable avec :
print(type(age2))


#type Float number

taille = 1.72
#Attention ne pas oublier str() pour les variable qui ne sont pas de type String
print("3-Ta tu fait "+str(taille)+" metres.")
#Tu peux verifier le type d'une variable avec :
print(type(taille))

#type Boolean

humain = True
#Attention ne pas oublier str() pour les variable qui ne sont pas de type String
print("4-Es-tu humain ? " + str(humain))
#Tu peux verifier le type d'une variable avec :
print(type(humain))
