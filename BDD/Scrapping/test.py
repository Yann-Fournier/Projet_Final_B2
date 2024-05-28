#  -----------------------------------------------------------------------------------------------------------------------
import pandas as pd

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

C = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
D = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

test1 = pd.DataFrame({"A": A, "B": B})

test1.to_csv("bidule.csv", encoding='utf-8')

test2 = pd.DataFrame({"A": C, "D": D})

test2.to_csv("bidule.csv", mode='a', header=False, encoding='utf-8')

test3 = pd.read_csv("bidule.csv")
# for i in range(len(test3)):
    # print(test3["A"][i], test3["B"][i])
    # print(test3.iloc[i])

livres = pd.read_csv("CSV/Save/Shōnen_combined.csv")
for i in range(len(livres)):
    print(livres["Auteur"][i])
    print("------------------")
#  -----------------------------------------------------------------------------------------------------------------------
# bidule = "Éditeur :"
# print(bidule.__contains__("Édi"))
# print("Éditeur ‏ : ‎ ")
# print(type("Éditeur ‏ : ‎ "))

#  -----------------------------------------------------------------------------------------------------------------------
# str = "https://www.amazon.fr/s?i=stripbooks&rh=n%3A27406977031&fs=true&page={}&ref=sr_pg_{}"
#
# for i in range(10):
#     print(str.format(i, i))

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

#  -----------------------------------------------------------------------------------------------------------------------
# test = {
#     "truc1": "bidule1",
#     "truc2": "bidule2",
#     "truc3": "bidule3"
# }
#
# for key, value in test.items():
#     print(key)
#     print(value)
#  -----------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# import json
#
# # Créez une instance de navigateur Chrome
# driver = webdriver.Chrome()
#
# driver.get('https://www.amazon.fr')
# time.sleep(10)
#
# driver.get('https://www.amazon.fr/gp/browse.html?node=301061&ref_=nav_em__lv_0_2_9_2')
# time.sleep(2)
#
# listBigCategories = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/div/div/ul')
# dictBigCategories = {}
#
# for category in listBigCategories:
#     print(category.text)
#     # "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/div/div/ul/li[2]"
#     # "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/div/div/ul/li[2]/span/span/div/a"
#     link = category.find_element(by=By.XPATH, value='./span/span/div/a').get_attribute('src')
#     titre = category.find_element(by=By.XPATH, value='./span/span/div/a/h3').text
#     if titre.__contains__("enfants") or titre.__contains__("Scolaire"):
#         pass
#     else:
#         print(titre, link)
#  -----------------------------------------------------------------------------------------------------------------------

# import json
# fichier_json = 'CSV/Categories.json'

# with open(fichier_json, 'w') as fichier:
#     json.dump(truc, fichier, indent=4)

# with open(fichier_json, 'r') as fichier_Pages:
#     contenu = fichier_Pages.read()
#     truc = json.loads(contenu)
#     print(truc)

#  -----------------------------------------------------------------------------------------------------------------------

# truc = "11,00 €"
# truc = truc[:-2]
# truc = truc.replace(',', '.')
# print(float(truc))

#  -----------------------------------------------------------------------------------------------------------------------
# import numpy as np

# # Générer un nombre flottant aléatoire entre 10.0 et 20.0
# nombre_aleatoire = np.random.uniform(10.0, 20.0)
# print(round(nombre_aleatoire, 2))


#  -----------------------------------------------------------------------------------------------------------------------
# import os

# # Chemin du dossier à explorer
# dossier = 'Scrapping/CSV/Save'

# # Liste pour stocker les chemins des fichiers
# fichiers = []

# # Boucle pour lister les fichiers dans le dossier
# for nom in os.listdir(dossier):
#     chemin_complet = os.path.join(dossier, nom)
#     if os.path.isfile(chemin_complet):
#         fichiers.append(nom)

# print(fichiers)
#
# import pandas as pd
# truc = pd.read_csv("CSV/Biographies.csv")
# print(truc)

#  -----------------------------------------------------------------------------------------------------------------------
# import json
# fichier_json_url_Categories = 'CSV/Categories.json'
# with open(fichier_json_url_Categories, 'r') as fichier_Categories:
#     contenuCategories = fichier_Categories.read()  # Le code bug si je ne transforme pas le json en str en premier
#     urlCategories = json.loads(contenuCategories)
#     Keys = urlCategories.keys()
# for i in Keys:
#     print(i)
# print(Keys)
