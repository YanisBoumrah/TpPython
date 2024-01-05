
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
    i["rate"] *= 1.01

# Creation de la fonction pour tirer aleatoirement une personne dans la liste
def random_person():
    return random.choice(populations)

# ordonner dans une liste les tuple
s = sorted([(person['name'], person['rate']) for person in populations], key=lambda x: x[1])

# calcule de la mediane des rates
def mediane():
    if len(s) % 2 == 0:
        return (s[len(s)//2][1] + s[len(s)//2-1][1])/2
    else:
        return s[len(s)//2][1]
    

# Partionnez la liste s en quatre parties distinctes
def partition():
    return [s[i*len(s)//4:(i+1)*len(s)//4] for i in range(4)]

#calcule de la moyenne des rates

def moyenne():
    return round(sum([person['rate'] for person in populations])/len(populations),2)

print (moyenne()) 

print (partition())