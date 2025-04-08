CREATE DATABASE IF NOT EXISTS bibliotheque CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE bibliotheque;

-- 👩‍🎓 Table : Étudiants
CREATE TABLE etudiants (
    id_etudiant INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

-- 👨‍🏫 Table : Enseignants
CREATE TABLE enseignants (
    id_enseignant INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

-- 👨‍💼 Table : Admins
CREATE TABLE admins (
    id_admin INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

-- 📚 Table : Livres
CREATE TABLE livres (
    id_livre INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    auteur VARCHAR(100) NOT NULL,
    genre VARCHAR(100),
    stock_disponible INT DEFAULT 0
);

-- 🔄 Table : Emprunts
CREATE TABLE emprunts (
    id_emprunt INT AUTO_INCREMENT PRIMARY KEY,
    id_livre INT NOT NULL,
    id_etudiant INT,
    id_enseignant INT,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    statut ENUM('en_cours', 'retourne') DEFAULT 'en_cours',
    FOREIGN KEY (id_livre) REFERENCES livres(id_livre),
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant)
);

-- 📆 Table : Réservations
CREATE TABLE reservations (
    id_reservation INT AUTO_INCREMENT PRIMARY KEY,
    id_livre INT NOT NULL,
    id_etudiant INT,
    id_enseignant INT,
    date_reservation DATE NOT NULL,
    statut ENUM('en_attente', 'annulée', 'confirmée') DEFAULT 'en_attente',
    FOREIGN KEY (id_livre) REFERENCES livres(id_livre),
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant)
);

-- 🔔 Table : Notifications
CREATE TABLE notifications (
    id_notification INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    date_envoi DATETIME NOT NULL,
    statut ENUM('non_lu', 'lu') DEFAULT 'non_lu',
    id_etudiant INT,
    id_enseignant INT,
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant)
);
