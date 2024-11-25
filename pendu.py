import json
import requests
import os

def GenerateWord(num):
    api_url = 'https://trouve-mot.fr/api/random/1'
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        for _ in range(num):
            response = requests.get(api_url)
            if response.status_code == requests.codes.ok:
                random_word = response.json() 
                data["words"].append(random_word[0]['name']) 
                print(f"Mot ajouté: {random_word[0]['name']}")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Updated JSON data:", data)
    except Exception as e:
        print(f"une erreur est apparu: {e}")

def viewJson(num):
    file = open('data.json')
    data = json.load(file) 
    print(data["words"])
    file.close()
    return data[num]



#GenerateWord(5)
#viewJson(2)
def compare(a, b):
    """
    Fonction qui vérifie si 'a' est présent dans 'b'.
    Retourne 1 si présent, sinon 0.
    """
    return 1 if a in b else 0

# Initialisation des variables
play = 1
lppb = []  # Lettre incorrecte
lpb = []   # Lettre correcte
k = 10     # Nombre d'essais
mad = "alright"  # Mot a découvrir
mot = ["_" for _ in mad]  # mot découvert
os.system('cls' if os.name == 'nt' else 'clear') #fonction universelle qui permet de clear l'ecran


# Configuration de la partie 

# Lancement du jeux 
while play == 1:
    # Affichage de l'état du mot
    print("Mot à deviner : " + " ".join(mot))
    letter = input("Propose une lettre : ").lower()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        continue

    if compare(letter, mad) == 1: 
        if letter not in lpb:  
            lpb.append(letter)
            
            for index, char in enumerate(mad):
                if char == letter:
                    mot[index] = letter
    else: 
        if letter not in lppb: 
            lppb.append(letter)
            k -= 1  
    os.system('cls' if os.name == 'nt' else 'clear')

    # affichage
    print(f"Nombre d'essais restants : {k}")
    #print("Lettres correctes : " + ", ".join(lpb))
    #print("Lettres incorrectes : " + ", ".join(lppb))

    # on va verifier si le mot est terminer
    if "_" not in mot:  
        print(f"Bien joué, tu as trouver le mot : {mad} !")
        play = 0
    elif k == 0:  
        print(f"T'es nul germain ! Le mot était : {mad}.")
        play = 0
