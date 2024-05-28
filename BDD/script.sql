DROP TABLE IF EXISTS Auth;
DROP TABLE IF EXISTS Users_Suivi;
DROP TABLE IF EXISTS Auteurs_Suivi;
DROP TABLE IF EXISTS Commentaires;
DROP TABLE IF EXISTS Collec;
DROP TABLE IF EXISTS Collections;
DROP TABLE IF EXISTS Livres;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Auteurs;
DROP TABLE IF EXISTS Users;


CREATE TABLE IF NOT EXISTS Users
(
    Id INTEGER,
    Email VARCHAR(100),
    Mdp VARCHAR(200),
    Photo VARCHAR(200),
    Nom VARCHAR(50),
    Is_Admin BOOL,

    PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS Auteurs
(
    Id INTEGER,
    Nom VARCHAR(50),
    Description VARCHAR(500),
    Photo VARCHAR(200),

    PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS Categories
(
    Id INTEGER,
    Nom VARCHAR(50),

    PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS Livres
(
    Id INTEGER,
    Id_Auteur INTEGER,
    Id_Categorie INTEGER,
    Nom VARCHAR(100),
    Description VARCHAR(500),
    Photo VARCHAR(200),
    ISBN VARCHAR(50),
    Editeur VARCHAR(100),
    Prix FLOAT,

    PRIMARY KEY (Id),
    FOREIGN KEY (Id_Auteur) REFERENCES Auteurs (Id),
    FOREIGN KEY (Id_Categorie) REFERENCES Categories (Id)
);

CREATE TABLE IF NOT EXISTS Collections
(
    Id INTEGER,
    Id_User INTEGER,
    Nom VARCHAR(100),
    Is_Private BOOL,

    PRIMARY KEY (Id),
    FOREIGN KEY (Id_User) REFERENCES Users (Id)
);

CREATE TABLE IF NOT EXISTS Collec
(
    Id_Livre INTEGER,
    Id_Collection INTEGER,

    FOREIGN KEY (Id_Livre) REFERENCES Livres (Id),
    FOREIGN KEY (Id_Collection) REFERENCES Collections (Id)
);

CREATE TABLE IF NOT EXISTS Commentaires
(
    Id INTEGER,
    Id_User INTEGER,
    Id_Livre INTEGER,
    Com VARCHAR(200),

    PRIMARY KEY (Id),
    FOREIGN KEY (Id_User) REFERENCES Users (Id),
    FOREIGN KEY (Id_Livre) REFERENCES Livres (Id)
);

CREATE TABLE IF NOT EXISTS Users_Suivi
(
    Id_User INTEGER,
    Id_User_Suivi INTEGER,

    FOREIGN KEY (Id_User) REFERENCES Users (Id),
    FOREIGN KEY (Id_User_Suivi) REFERENCES Users (Id)
);


CREATE TABLE IF NOT EXISTS Auteurs_Suivi
(
    Id_User INTEGER,
    Id_Auteur INTEGER,

    FOREIGN KEY (Id_User) REFERENCES Users (Id),
    FOREIGN KEY (Id_Auteur) REFERENCES Auteurs (Id)
);

CREATE TABLE IF NOT EXISTS Auth
(
    Id INT,
    Token VARCHAR(100),

    FOREIGN KEY (Id) REFERENCES Users (Id)
)