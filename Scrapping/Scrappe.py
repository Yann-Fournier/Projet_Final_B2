from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def rechercheTab(tab, str):
    for var in tab:
        if var == str:
            return True
    return False

# Créez une instance de navigateur Chrome
driver = webdriver.Chrome()

categories = ['Shōnen']
urlCategories = ['https://www.amazon.fr/s?i=stripbooks&rh=n%3A27406977031&fs=true&page=1&ref=sr_pg_1']

# Configuration --------------------------------------------------------------------------------------
driver.get('https://www.amazon.fr')
time.sleep(20)

driver.get(urlCategories[0])
time.sleep(1)
nbrPage = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[18]/div/div/span/span[4]').text.strip())
print(nbrPage)  # Nombre de pages web pour faire tout le scrapping

# Initialisation tableau auteur -------------------------------------------------------------------------
nomAuteur = []
photoAuteur = []
descAuteur = []

#  Boucle ---------------------------------------------------------------------------------------------
# for i in range(1, nbrPage+1):
for i in range(1, 2):
    # Initialisation tableaux à chaque nouvelle page -------------------------------------------------------------------
    nom = []
    description = []
    photo = []
    isbn = []
    editeur = []
    prix = []
    auteur = []

    # On va sur chacun des pages
    driver.get(f"https://www.amazon.fr/s?i=stripbooks&rh=n%3A27406977031&fs=true&page={str(i)}&ref=sr_pg_{str(i)}")
    time.sleep(1)

    #  Page simple -------------------------------------------------------------------------------
    # Je divise la recupération des liens en deux requêtes, car sinon les xpath est trop grand et l'IDE n'est pas content
    divPrincipal = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]')
    divs = divPrincipal.find_elements(By.CLASS_NAME, 's-widget-spacing-small')
    linksInPage = []  # tableau des liens des livres de la page actuelle

    for div in divs:  # recuperation des liens des livres de la page actuelle
        try:
            xpath = './div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a'  # chemin relatif
            elm = div.find_element(By.XPATH, xpath).text
        except:
            xpath = './div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/a'  # chemin relatif
            elm = div.find_element(By.XPATH, xpath).text

        if (elm == "Poche" or elm == "Relié" or elm == "Broché"):
            linksInPage.append(div.find_element(By.XPATH, './div/div/span/div/div/div/div[1]/div/div[2]/div/span/a').get_attribute('href'))
    print(i, ":", len(linksInPage), "--------------------------------------------------------------------------------------")

    cpt = 0  # tkt
    for link in linksInPage:
        cpt += 1  # tkt
        # On va sur chacune des pages des livres pour récupérer les infos qui nous interesse.
        driver.get(link)
        time.sleep(2)
        try:
            name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[8]/div[2]/div/h1/span[1]').text
            nom.append(name)
        except:
            nom.append("")
        try:
            desc = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/div[8]/div[28]/div[1]/div/div[1]/span').text
            description.append(desc)
        except:
            description.append("Descripton non disponible")
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
            if rechercheTab(nomAuteur, aut) == False:
                nomAuteur.append(aut)
                try:
                    descAut = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[25]/div[2]/div').text
                    descAuteur.append(descAut)
                except:
                    descAuteur.append("Description non disponible")
                try:
                    picAut = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[28]/div/div/div[2]/div/div/div/div[1]/div[1]/div/img').get_attribute('src')
                    photoAuteur.append(picAut)
                except:
                    photoAuteur.append("")
        except:
            auteur.append("")
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
                price = 7.99
        prix.append(float(price))

        print(cpt, "/", len(linksInPage))

    print("")
    print("nom", len(nom))
    print("description", len(description))
    print("photo", len(photo))
    print("isbn", len(isbn))
    print("editeur", len(editeur))
    print("prix", len(prix))
    print("auteur", len(auteur))
    print("")
    print("nomAuteur", len(nomAuteur))
    print("descAuteur", len(descAuteur))
    print("photoAuteur", len(photoAuteur))

    dfLivres = pd.DataFrame({"Nom": nom, "Prix": prix, "Description": description, "Isbn": isbn, "Photo": photo, "Editeur": editeur, "Auteur": auteur})
    dfLivres.drop_duplicates(ignore_index=True, inplace=True)
    fileNameLivres = 'CSV/Shonen/shonen' + str(i) + '.csv'
    dfLivres.to_csv(fileNameLivres, index=False, encoding='utf-8')

dfAuteur = pd.DataFrame({"Nom": nomAuteur, "Description": descAuteur, "Photo": photoAuteur})
dfAuteur.drop_duplicates(ignore_index=True, inplace=True)
fileNameAuteur = 'CSV/Auteurs/AuteursShonen.csv'
dfAuteur.to_csv(fileNameAuteur, index=False, encoding='utf-8')

# Fermer le navigateur
driver.quit()

# -------------------------------------------------------------------------------------------------------------------
# la récupération des éléments de la liste des détails
# la conversion du prix : string to float
# -------------------------------------------------------------------------------------------------------------------



