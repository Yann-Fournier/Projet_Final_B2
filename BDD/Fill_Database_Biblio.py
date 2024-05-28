from faker import Faker
import pandas as pd
import sqlite3
import hashlib
import json

conn = sqlite3.connect('Database_Biblio.db')  # Se connecter à la base de données
cur = conn.cursor()  # Créer un curseur


def load_sql():
    with open("script.sql", 'r') as fichier:
        script_sql = fichier.read()

    try:
        cur.executescript(script_sql)  # execution du script
        conn.commit()  # enregistrement des changements
        print("Script SQL exécuté avec succès")

    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")


def load_data():
    # 5 Users (3 admins et 2 normaux)
    insert_user(0, "admin@biblio.com", hash_passwd("admin1234"), "", "Admin", True)
    insert_user(1, "yann.fournier@biblio.com", hash_passwd("yann1234"), "", "Yann Fournier", True)
    insert_user(2, "adriana.fournier@biblio.com", hash_passwd("adriana1234"), "", "Adriana Pullig", True)

    insert_user(3, "yann@ynov.com", hash_passwd("yann"), "", "Yann", False)
    insert_user(4, "adriana@ynov.com", hash_passwd("adriana"), "", "Adriana", False)

    # Token d'Auth
    insert_auth(0, hash_passwd("Admin"))
    insert_auth(1, hash_passwd("Yann Fournier"))
    insert_auth(2, hash_passwd("Adriana Pullig"))
    
    insert_auth(3, hash_passwd("Yann"))
    insert_auth(4, hash_passwd("Adriana"))
    
    # Toutes les catégories
    fichier_json_url_categories = 'Scrapping/CSV/Categories.json'
    with open(fichier_json_url_categories, 'r') as fichier_categories:
        contenu_categories = fichier_categories.read()  # Le code bug si je ne transforme pas le json en str en premier
        url_categories = json.loads(contenu_categories)
        keys = url_categories.keys()

    cpt = 0
    for key in keys:
        insert_categorie(cpt, key)
        cpt += 1

    # Tous les Auteurs
    auteurs = pd.read_csv("Scrapping/CSV/Save/Auteurs_combined.csv")
    for i in range(len(auteurs)):
        insert_auteur(i, auteurs["Nom"][i], auteurs["Description"][i], auteurs["Photo"][i])

    # Tous les Livres
    livres = pd.read_csv("Scrapping/CSV/Save/Shōnen_combined.csv")
    cur.execute("SELECT Id FROM Categories WHERE Nom = 'Shōnen';")  # Id = 55
    results_id_category = cur.fetchall()  # renvoie un tableau de tuple
    for i in range(len(livres)):
        query = "SELECT Id FROM Auteurs WHERE Nom = '" + str(livres["Auteur"][i]) + "';"
        cur.execute(query)
        results_id_auteur = cur.fetchall()  # renvoie un tableau de tuple
        insert_livre(i, results_id_auteur[0][0], results_id_category[0][0], str(livres["Nom"][i]),
                     str(livres["Description"][i]), str(livres["Photo"][i]), str(livres["Isbn"][i]),
                     str(livres["Editeur"][i]), float(livres["Prix"][i]))

    # Toutes les collections
    insert_collection(0, 3, "J'ai", True)
    insert_collection(1, 3, "Ma pile à lire", True)
    insert_collection(2, 3, "Je lis", True)
    insert_collection(3, 3, "J'ai lu", True)
    insert_collection(4, 3, "J'aime", True)
    insert_collection(5, 3, "Ma liste de souhait", True)

    insert_collection(6, 4, "J'ai", True)
    insert_collection(7, 4, "Ma pile à lire", True)
    insert_collection(8, 4, "Je lis", True)
    insert_collection(9, 4, "J'ai lu", True)
    insert_collection(10, 4, "J'aime", True)
    insert_collection(11, 4, "Ma liste de souhait", True)

    # Liste des collections
    insert_collec(0, 0)
    insert_collec(1, 0)
    insert_collec(2, 0)
    insert_collec(0, 1)
    insert_collec(1, 1)
    insert_collec(2, 1)

    insert_collec(3, 6)
    insert_collec(4, 6)
    insert_collec(5, 6)
    insert_collec(3, 7)
    insert_collec(4, 7)
    insert_collec(5, 7)

    # Commentaires
    for i in range(len(livres)):
        insert_commentaires(3, i, "Ce livre est génial. :)")
        insert_commentaires(4, i, "J'adore ce livre. Il a vraiment changer ma vie !!!!!!")

    # Ajout de certains Auteurs suivis
    insert_users_suivi(3, 4)
    insert_users_suivi(4, 3)

    # Ajout de certains Users suivis
    insert_auteurs_suivi(3, 0)
    insert_auteurs_suivi(3, 1)
    insert_auteurs_suivi(3, 2)
    insert_auteurs_suivi(3, 3)
    insert_auteurs_suivi(3, 4)
    insert_auteurs_suivi(4, 5)
    insert_auteurs_suivi(4, 6)
    insert_auteurs_suivi(4, 7)
    insert_auteurs_suivi(4, 8)
    insert_auteurs_suivi(4, 9)

    print("Load des données bien exécuter")


def hash_passwd(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def insert_user(Id, Email, Mdp, Photo, Nom, Is_Admin, data=None):
    if data is None:
        data = [
            Id, Email, Mdp, Photo, Nom, Is_Admin
        ]
    conn.execute(
        "INSERT INTO Users (Id, Email, Mdp, Photo, Nom, Is_Admin) VALUES(?, ?, ?, ?, ?, ?)", data)
    conn.commit()


def insert_auteur(Id, Nom, Description, Photo, data=None):
    if data is None:
        data = [
            Id, Nom, Description, Photo
        ]
    conn.execute(
        "INSERT INTO Auteurs (Id, Nom, Description, Photo) VALUES(?, ?, ?, ?)", data)
    conn.commit()


def insert_categorie(Id, Nom, data=None):
    if data is None:
        data = [
            Id, Nom
        ]
    conn.execute(
        "INSERT INTO Categories (Id, Nom) VALUES(?, ?)", data)
    conn.commit()


def insert_livre(Id, Id_Auteur, Id_Categorie, Nom, Description, Photo, ISBN, Editeur, Prix, data=None):
    if data is None:
        data = [
            Id, Id_Auteur, Id_Categorie, Nom, Description, Photo, ISBN, Editeur, Prix
        ]
    conn.execute(
        "INSERT INTO Livres (Id, Id_Auteur, Id_Categorie, Nom, Description, Photo, ISBN, Editeur, Prix) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()


def insert_collection(Id, Id_User, Nom, Is_Private, data=None):
    if data is None:
        data = [
            Id, Id_User, Nom, Is_Private
        ]
    conn.execute(
        "INSERT INTO Collections (Id, Id_User, Nom, Is_Private) VALUES(?, ?, ?, ?)", data)
    conn.commit()


def insert_collec(Id_Livre, Id_Collection, data=None):
    if data is None:
        data = [
            Id_Livre, Id_Collection
        ]
    conn.execute(
        "INSERT INTO Collec (Id_Livre, Id_Collection) VALUES(?, ?)", data)
    conn.commit()


def insert_commentaires(Id_User, Id_Livre,Com, data=None):
    if data is None:
        data = [
            Id_User, Id_Livre, Com
        ]
    conn.execute(
        "INSERT INTO Commentaires (Id_User, Id_Livre, Com) VALUES(?, ?, ?)", data)
    conn.commit()


def insert_users_suivi(Id_User, Id_User_Suivi, data=None):
    if data is None:
        data = [
            Id_User, Id_User_Suivi
        ]
    conn.execute(
        "INSERT INTO Users_Suivi (Id_User, Id_User_Suivi) VALUES(?, ?)", data)
    conn.commit()


def insert_auteurs_suivi(Id_User, Id_Auteur, data=None):
    if data is None:
        data = [
            Id_User, Id_Auteur
        ]
    conn.execute(
        "INSERT INTO Auteurs_Suivi (Id_User, Id_Auteur) VALUES(?, ?)", data)
    conn.commit()


def insert_auth(Id, Token, data=None):
    if data is None:
        data = [
            Id, Token
        ]
    conn.execute(
        "INSERT INTO Auth (Id, Token) VALUES(?, ?)", data)
    conn.commit()
    
#  Fonction pour remplir la database -----------------------------------------------------------------------------------
load_sql()
load_data()


# Fermer le curseur et la connexion ------------------------------------------------------------------------------------
cur.close()
conn.close()
