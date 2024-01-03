
from random import randint
import random

populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]

# Ajouter le champ lenChar au dictionnaire
for i in populations:
    i["lenChar"] = len(i["name"])


# Ajout d'un champ rate au dictionnaire 
for i in populations:
    i["rate"] = randint(0, 10)
    
# Determiner les 4 personnes avec le meilleur rate
top_rated = sorted(populations, key=lambda x: x['rate'], reverse=True)[:4]

#Attribution d'une augmentation de 0,1% a toute la population

for i in populations:
    i["rate"] *= 1.001

# Creation de la fonction pour tirer aleatoirement une personne dans la liste
def random_person():
    return random.choice(populations)

print(random_person())