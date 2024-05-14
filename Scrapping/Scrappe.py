from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
print(nbrPage) # Nombre de page web pour faire tout le scrapping

# Initialisation tableaux -------------------------------------------------------------------------------
nom = []
description = []
photo = []
isbn = []
editeur = []
prix = []

#  Boucle ---------------------------------------------------------------------------------------------
for i in range(1, nbrPage+1):
    # On va sur chacun des pages
    driver.get(f"https://www.amazon.fr/s?i=stripbooks&rh=n%3A27406977031&fs=true&page={str(i)}&ref=sr_pg_{str(i)}")
    time.sleep(1)

    #  Page simple -------------------------------------------------------------------------------
    # Je divise la recupération des lien en deux requêtes car sinon les xpath est trop grand et l'IDE est pas content
    divPrincipal = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]')
    divs = divPrincipal.find_elements(By.CLASS_NAME, 's-widget-spacing-small')
    linksInPage = [] # tableau des lien des livres de la page actuelle

    for div in divs:  # recuperation des lien des livres de la page actuelle
        try:
            xpath = './div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a'  # chemin relatif
            elm = div.find_element(By.XPATH, xpath).text
        except:
            xpath = './div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/a'  # chemin relatif
            elm = div.find_element(By.XPATH, xpath).text

        if (elm == "Poche" or elm == "Relié" or elm == "Broché"):
            linksInPage.append(div.find_element(By.XPATH, './div/div/span/div/div/div/div[1]/div/div[2]/div/span/a').get_attribute('href'))
    print(i, ":", len(linksInPage))

    for link in linksInPage: # On va sur chacune des pages des livres pour récupérer les infos qui nous interresse.
        driver.get(link)
        time.sleep(1)

# Fermez le navigateur
driver.quit()