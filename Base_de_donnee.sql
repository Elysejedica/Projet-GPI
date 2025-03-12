CREATE DATABASE Bibliotheque;
USE Bibliotheque;
//alao utilusateur io de solohy enseignant ndraiky etudiants 
CREATE TABLE Utilisateurs (
    id_utilisateur INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('membre', 'bibliothecaire') DEFAULT 'membre'
);

CREATE TABLE Livres (
    id_livre INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(100),
    genre VARCHAR(100),
    stock_disponible INT DEFAULT 1
);

CREATE TABLE Reservations (
    id_reservation INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur INT,
    id_livre INT,
    date_reservation DATE NOT NULL DEFAULT (CURRENT_DATE),
    statut ENUM('en attente', 'confirmée', 'annulée') DEFAULT 'en attente',
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES Livres(id_livre) ON DELETE CASCADE
);

CREATE TABLE Emprunts (
    id_emprunt INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur INT,
    id_livre INT,
    date_emprunt DATE NOT NULL DEFAULT (CURRENT_DATE),
    date_retour_prevue DATE NOT NULL,
    statut ENUM('en cours', 'retourné') DEFAULT 'en cours',
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES Livres(id_livre) ON DELETE CASCADE
);

CREATE TABLE Notifications (
    id_notification INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur INT,
    message TEXT NOT NULL,
    date_envoi DATETIME NOT NULL DEFAULT NOW(),
    statut ENUM('envoyée', 'vue') DEFAULT 'envoyée',
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur) ON DELETE CASCADE
);
