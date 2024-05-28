from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import json
import numpy as np

# Faire les paths multiples pour toutes les différentes infos à récuperer (nom, Desc, Auteur, photo, etc ...)
# Créez une instance de navigateur Chrome
driver = webdriver.Chrome()

fichier_json_url_Categories = 'CSV/Categories.json'
fichier_json_Pages = 'CSV/Pages.json'
# fichier_json_url_Categories = 'Scrapping/CSV/Categories.json'
# fichier_json_Pages = 'Scrapping/CSV/Pages.json'
with open(fichier_json_url_Categories, 'r') as fichier_Categories:
    contenuCategories = fichier_Categories.read()  # Le code bug si je ne transforme pas le json en str en premier
    urlCategories = json.loads(contenuCategories)
with open(fichier_json_Pages, 'r') as fichier_Pages:
    contenuPages = fichier_Pages.read()  # Le code bug si je ne transforme pas le json en str en premier
    indicesPagesPasPrises = json.loads(contenuPages)  # Les indices des pages qui n'ont pas été scrapper à cause de PB

# Configuration --------------------------------------------------------------------------------------------------------
driver.get('https://www.amazon.fr')
time.sleep(20)

#  Boucle des catégories --------------------------------------------------------------------
for key, value in urlCategories.items():

    print(key)
    indicesPagesPasPrises2 = []
    #  Boucle des pages --------------------------------------------------------------------------------------------------------------
    for i in range(1, 76):
    # for i in range(1, 2):
        # Initialisation tableaux à chaque nouvelle page -------------------------------------------------------------------
        nom = []
        description = []
        photo = []
        isbn = []
        editeur = []
        prix = []
        auteur = []
        categorie = []

        # Initialisation tableau auteur ------------------------------------------------------------------------------------
        nomAuteur = []
        photoAuteur = []
        descAuteur = []

        try:
            # On va sur chacun des pages
            driver.get(value.format(i, i))
            time.sleep(10)

            #  Page simple -------------------------------------------------------------------------------------------------
            # Je divise la recupération des liens en deux requêtes, car sinon les xpath est trop grand et l'IDE n'est pas content
            divPrincipal = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]')
            divs = divPrincipal.find_elements(By.CLASS_NAME, 's-widget-spacing-small')
            linksInPage = []  # tableau des liens des livres de la page actuelle

            for div in divs: # recuperation des liens des livres de la page actuelle
                try:
                    elm = div.find_element(By.XPATH, './div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a').text  # chemin relatif
                except:
                    elm = div.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a').text  # chemin complet

                if (elm == "Poche" or elm == "Relié" or elm == "Broché" or elm == "Carte"):
                    try:
                        linksInPage.append(div.find_element(By.XPATH, './div/div/span/div/div/div/div[1]/div/div[2]/div/span/a').get_attribute('href'))  # chemin relatif
                    except:
                        linksInPage.append(div.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a').get_attribute('href')) # chemin complet
            print(i, ":", len(linksInPage), "--------------------------------------------------------------------------------------")

            cpt = 0  # tkt
            for link in linksInPage:
                cpt += 1  # tkt
                # On va sur chacune des pages des livres pour récupérer les infos qui nous interesse.
                driver.get(link)
                time.sleep(10)
                try:
                    name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[8]/div[2]/div/h1/span[1]').text
                    nom.append(name)
                except:
                    nom.append("")
                try:
                    desc = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[8]/div[28]/div[1]/div/div[1]/span').text
                    description.append(desc)
                except:
                    description.append("")
                try:
                    pic = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[7]/div[1]/div[1]/div/div/div/div[1]/div[1]/ul/li[1]/span/span/div/img').get_attribute('src')
                    photo.append(pic)
                except:
                    photo.append("")
                try:
                    details = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[4]/div[26]/div/div[1]/ul/li')
                    for det in details:
                        truc = det.find_element(By.XPATH, './span/span[1]').text
                        # print(truc)
                        if truc.__contains__("ISBN-13"):
                            isbn.append(det.find_element(By.XPATH, './span/span[2]').text)
                        elif truc.__contains__("Éditeur"):
                            editeur.append(det.find_element(By.XPATH, './span/span[2]').text)
                except:
                    isbn.append("")
                    editeur.append("")

                try:
                    aut = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[8]/div[3]/div/span[1]/a').text
                    auteur.append(aut)
                    nomAuteur.append(aut)
                except:
                    auteur.append("")
                try:
                    descAut = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[25]/div[2]/div').text
                    descAuteur.append(descAut)
                except:
                    descAuteur.append("")
                try:
                    picAut = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[28]/div/div/div[2]/div/div/div/div[1]/div[1]/div/img').get_attribute('src')
                    photoAuteur.append(picAut)
                except:
                    photoAuteur.append("")

                price = 0.0
                try:
                    priceInt = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/form/div/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[1]').text
                    priceFloat = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/form/div/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[2]').text
                    price = priceInt + "." + priceFloat
                    price = float(price)
                except:
                    price = 0.0
                if price == 0.0:
                    try:
                        priceInt = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[1]').text
                        priceFloat = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[2]').text
                        price = priceInt + "." + priceFloat
                        price = float(price)
                    except:
                        price = 0.0
                if price == 0.0:
                    try:
                        priceInt = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div[2]/div/div/div/div/div/form/div/div/div/div/div[4]/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[1]').text
                        priceFloat = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[4]/div/div[1]/div/div[2]/div/div/div/div/div/form/div/div/div/div/div[4]/div/div[2]/div[1]/div[1]/span[2]/span[2]/span[2]').text
                        price = priceInt + "." + priceFloat
                        price = float(price)
                    except:
                        price = 0.0
                if price == 0.0:
                    try:
                        priceSTR = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[2]/div/div/div/div[2]/span/span/a/span[2]/span')
                        priceSTR = priceSTR[:-2]
                        priceSTR = priceSTR.replace(',', '.')
                        price = float(priceSTR)
                    except:
                        price = 0.0
                if price == 0.0:
                    try:
                        priceSTR = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[5]/div[4]/div[2]/div/div/div[2]/div[2]/span/span/a/span[2]/span')
                        priceSTR = priceSTR[:-2]
                        priceSTR = priceSTR.replace(',', '.')
                        price = float(priceSTR)
                    except:
                        price = 0.0
                if price == 0.0:
                    nombre_aleatoire = np.random.uniform(5.0, 20.0)
                    price = round(nombre_aleatoire, 2)
                print(price)
                prix.append(price)
                categorie.append(key)

                print(cpt, "/", len(linksInPage))

            if len(nom) == len(description) == len(photo) == len(isbn) == len(editeur) == len(prix) == len(auteur):
                time.sleep(1)
                dfLivres = pd.DataFrame({"Nom": nom, "Prix": prix, "Description": description, "Isbn": isbn, "Photo": photo, "Editeur": editeur, "Auteur": auteur})
                fileNameLivres = 'CSV/' + key + '.csv'
                # fileNameLivres = "Scrapping/CSV/Shonen/" + str(key) + ".csv"
                if i == 1:
                    dfLivres.to_csv(fileNameLivres, index=False, encoding='utf-8')
                else:
                    dfLivres.to_csv(fileNameLivres, mode='a', index=False, header=False, encoding='utf-8')
            else:
                # indicesPagesPasPrises[key].append(i)
                print("Len livres pas OK")
                print(len(nom))
                print(len(description))
                print(len(photo))
                print(len(isbn))
                print(len(editeur))
                print(len(prix))
                print(len(auteur))
                indicesPagesPasPrises2.append(i)

            if len(nomAuteur) == len(descAuteur) == len(photoAuteur):
                time.sleep(1)
                dfAuteur = pd.DataFrame({"Nom": nomAuteur, "Description": descAuteur, "Photo": photoAuteur})
                fileNameAuteur = 'CSV/Auteurs' + key + '.csv'
                # fileNameAuteur = "Scrapping/CSV/Auteurs" + str(key) + ".csv"
                if i == 1:
                    dfAuteur.to_csv(fileNameAuteur, index=False, encoding='utf-8')
                else:
                    dfAuteur.to_csv(fileNameAuteur,  mode='a', index=False, header=False, encoding='utf-8')
            else:
                print("Len auteurs pas OK")
                print(len(nomAuteur))
                print(len(descAuteur))
                print(len(photoAuteur))
        except:
            print("PB recupération des liens des livres")
            # indicesPagesPasPrises[key].append(i)
            indicesPagesPasPrises2.append(i)

        #  Sauvegarde des pages qui n'ont pas été scrapper par catégories--------------------------------------------------
        indicesPagesPasPrises[key] = indicesPagesPasPrises2
    with open(fichier_json_Pages, 'w') as fichier:
        json.dump(indicesPagesPasPrises, fichier, indent=4)

    

# Fermer le navigateur
driver.quit()
print("Le scrap est fini !!!!!!!!!!!!!!!!!")


# ----------------------------------------------------------------------------------------------------------------------
# la récupération des éléments de la liste des détails
# la conversion du prix : string to float
# -------------------------------------------------------------------------------------------------------------------



