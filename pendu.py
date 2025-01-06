import json
import requests
import os

def GenerateWord(num): #on prend en parametre le nombre de mot qu'on souhaite générer
    api_url = f'https://trouve-mot.fr/api/random/{num}'
    print(api_url)
    try:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file) 
        except FileNotFoundError: # on gére les erreurs potentiels
            data = {"words": []} 
        
        
        data["words"] = [] # on clear le json

        
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            random_words = response.json()  
            for word in random_words:
                data["words"].append(word['name'])  
                print(f"Mot ajouté: {word['name']}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return  
        
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Mise a jour du JSON : ", data)
    except Exception as e: # on gére les erreurs potentiels
        print(f"Une erreur est survenue: {e}")

def viewJson(): # on va prendre en params
    file = open('data.json')
    data = json.load(file) 
    print(data["words"])
    file.close()
    return data["words"]


#GenerateWord(1)
def compare(a, b):
    return 1 if a in b else 0

def Change_Params(p,v): # prend en parametre le nom du params : p, et v, la valeur
    try:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file) 
        except FileNotFoundError: # on gére les erreurs potentiels
            print("fichier Json non trouvé")
            return
        
        
        data["params"] = [] # on clear le json
           

        
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Mise a jour du JSON : ", data)
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
# Initialisation des variables et de la partie


print(r"""

                 _                       _         ____                _       
                | | ___ _   ___  __   __| |_   _  |  _ \ ___ _ __   __| |_   _ 
             _  | |/ _ \ | | \ \/ /  / _` | | | | | |_) / _ \ '_ \ / _` | | | |
            | |_| |  __/ |_| |>  <  | (_| | |_| | |  __/  __/ | | | (_| | |_| |
             \___/ \___|\__,_/_/\_\  \__,_|\__,_| |_|   \___|_| |_|\__,_|\__,_|
                                                                    By Maxime & Hugo
""")

print("vous souhaitez :")
print("1) Définir le mot manuellement")
print("2) Génerer le mot automatiquement")
print("3) Acceder au Paramètres du jeux")
print("4) Fermer le jeux")
reponse_input = int(input())

if reponse_input == 1: 
    mad = input("Veuillez choisir le mot : ")
elif reponse_input == 2:
    GenerateWord(1)
    mad = viewJson()[0]
    print(mad)
elif reponse_input == 3:
    print("Paramètre ")
    print("1) Définir le nombre de vie") 
    response_params = input()
    if response_params == 1 : # Ce bout de code est pas propre et me fait mal a la tête, mais je suis limité par le temp
        input()
elif reponse_input == 4:
    print("fermeture du programme..")
else: 
    print("mauvaise reponse")


play = 1
lppb = []  # Lettre incorrecte
lpb = []   # Lettre correcte
k = 10     # Nombre d'essais
mot = ["_" for _ in mad]  # mot découvert
os.system('cls' if os.name == 'nt' else 'clear') #fonction universelle qui permet de clear l'ecran





# Lancement du jeux 
#while numberofword == data['words']
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
