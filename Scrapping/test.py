#  -----------------------------------------------------------------------------------------------------------------------
# import pandas as pd
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# C = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# D = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# test1 = pd.DataFrame({"A": A, "B": B})
#
# test1.to_csv("bidule.csv", index=False, encoding='utf-8')
#
# test2 = pd.DataFrame({"A": C, "D": D})
#
# test2.to_csv("bidule.csv", mode='a', index=False, header=False, encoding='utf-8')

#  -----------------------------------------------------------------------------------------------------------------------
# bidule = "Éditeur :"
# print(bidule.__contains__("Édi"))
# print("Éditeur ‏ : ‎ ")
# print(type("Éditeur ‏ : ‎ "))

#  -----------------------------------------------------------------------------------------------------------------------
str = "https://www.amazon.fr/s?i=stripbooks&rh=n%3A27406977031&fs=true&page={}&ref=sr_pg_{}"

for i in range(10):
    print(str.format(i, i))

#  -----------------------------------------------------------------------------------------------------------------------
# import json
#
# # Nouvelles données à ajouter
# nouvelles_donnees = {
#     "nom": "Bob",
#     "age": 25,
#     "profession": "Designer",
#     "langages": ["JavaScript", "HTML", "CSS"]
# }
#
# # Chemin du fichier JSON
# fichier_json = 'CSV/Pages.json'
#
# # Écrire le tout dans le fichier
# with open(fichier_json, 'w') as fichier:
#     json.dump(nouvelles_donnees, fichier, indent=4)
#
# with open(fichier_json, 'r') as fichier:
#     nouvelles_donnees = json.load(fichier)
#
# nouvelles_donnees["nom"] = "Autre"
# # Écrire le tout dans le fichier
# with open(fichier_json, 'w') as fichier:
#     json.dump(nouvelles_donnees, fichier, indent=4)
#
# print(f"Les nouvelles données ont été ajoutées à {fichier_json}")


