Cahier des Charges
Projet : Gestion des Contacts avec Django
1. Présentation du Projet
Contexte :
Le projet consiste à développer une application web de gestion des contacts
permettant d’effectuer des opérations CRUD (Créer, Lire, Mettre à jour,
Supprimer). Chaque contact sera défini par un prénom, un nom, un numéro de
téléphone, le réseau (Airtel ou MTN) et une catégorie (Famille, Professionnel,
Autres). L’application sera réalisée avec le framework Django, en respectant
l’architecture MTV (Modèle, Template, Vue) et les bonnes pratiques de
développement web.
Public cible :
Les utilisateurs souhaitant gérer leurs contacts (personnel ou professionnel).
Les équipes administratives ou commerciales d’une entreprise.

2. Objectifs du Projet
Objectifs fonctionnels
Création d’un contact :
Mise en place d’un formulaire de saisie avec les champs : Prénom, Nom,
Numéro de téléphone, Réseau (Airtel ou MTN), et Catégorie (Famille,
Professionnel, Autres).
Validation des données (format du numéro de téléphone, sélection
obligatoire du réseau et de la catégorie, présence des champs Prénom
et Nom).
Redirection vers la liste des contacts après création.
Lecture des contacts :
Liste des contacts : Affichage de tous les contacts avec leurs informations
principales (Prénom et Nom, Numéro de téléphone).Détail d’un contact : Affichage détaillé du contact sélectionné, incluant
tous les champs.
Mise à jour d’un contact :
Formulaire pré-rempli permettant la modification des informations du
contact.
Suppression d’un contact :
Page de confirmation avant suppression définitive.
Suppression effective avec redirection vers la liste des contacts.
Objectifs non fonctionnels (Technique)
Interface ergonomique et responsive :
L’application devra être accessible et utilisable sur ordinateur, tablette et
smartphone.
Sécurité :
Utilisation du token CSRF pour protéger les formulaires.
Validation et nettoyage des données côté serveur.
Modularité et maintenabilité :
Respect de l’architecture Django (séparation claire entre modèles, vues,
templates).
Utilisation de vues génériques pour limiter le code redondant.

3. Périmètre Fonctionnel

3.1 Gestion des Contacts (CRUD)
Création d’un contact :
Formulaire de saisie avec les champs :
Prénom : Champ texte.
Nom : Champ texte.
Numéro de téléphone : Champ texte avec validation.
Réseau : Liste déroulante proposant "Airtel" et "MTN".
Catégorie : Liste déroulante proposant "Famille", "Professionnel" et
"Autres".
Lecture des contacts :Liste des contacts :
Affichage de la liste des contacts sous forme de tableau ou de liste.
Chaque ligne affiche le Prénom et le Nom, ainsi que le Numéro de
téléphone, avec des liens vers les pages de détail, modification et
suppression.
Détail d’un contact :
Affichage complet des informations : Prénom, Nom, Numéro de
téléphone, Réseau et Catégorie.
Mise à jour d’un contact :
Formulaire pré-rempli avec les données actuelles du contact, permettant
la modification de chaque champ.
Suppression d’un contact :
Affichage d’une page de confirmation avant suppression définitive.
3.2 Navigation et Ergonomie
Interface globale :
Utilisation d’un template de base ( base.html ) incluant un header, un
footer et une barre de navigation.
Navigation intuitive avec des liens directs vers la liste des contacts et le
formulaire de création.
Accessibilité et Responsivité :
Design responsive pour un affichage correct sur tous types d’appareils.
Structure de navigation hiérarchisée et claire.

4. Spécifications Techniques

4.1 Architecture et Technologies
Framework :
Django (version stable recommandée).
Langage :
Python (version compatible avec Django).
Base de données :
SQLite pour le développement ou MySQL/PostgreSQL en production.Modèle de données :
Contact avec les champs :
prenom : CharField (max_length=100)
nom : CharField (max_length=100)
telephone : CharField (max_length=20)
reseau : CharField avec choix (par exemple, choices=[("Airtel",
"Airtel"), ("MTN", "MTN")] )
categorie : CharField avec choix (par exemple, choices=[("Famille",
"Famille"), ("Professionnel", "Professionnel"), ("Autres",
"Autres")] )
created_at : DateTimeField (auto_now_add=True)

4.2 Organisation du Code
Projet Django :
Nom du projet : gestion_contacts
Application :
Nom de l’application : contacts

5. Maquettes et Interfaces Utilisateur

5.1 Maquette de la Page d’Accueil (Liste des Contacts)
Header :
Titre "Gestion des Contacts".
Menu de navigation avec un lien vers la liste des contacts et vers le
formulaire de création.
Liste des contacts :
Affichage sous forme de liste ou tableau.
Chaque entrée affiche le Prénom, le Nom et le Numéro de téléphone.
Boutons ou liens pour accéder aux pages de détail, modification et
suppression.

5.2 Maquette du Formulaire de Contact
Champs de saisie :Prénom
Nom
Numéro de téléphone
Réseau : Liste déroulante (options : Airtel, MTN).
Catégorie : Liste déroulante (options : Famille, Professionnel, Autres).
Boutons d’action :
"Enregistrer" pour soumettre le formulaire.
"Annuler" pour revenir à la liste des contacts.

5.3 Maquette de la Page de Détail
Informations affichées :
Prénom, Nom, Numéro de téléphone, Réseau et Catégorie.
Boutons d’action :
"Modifier" pour accéder au formulaire de mise à jour.
"Supprimer" pour accéder à la confirmation de suppression.
"Retour" pour revenir à la liste des contacts.

6. Planning et Livrables

6.1 Planning Prévisionnel
PhaseDurée estimée
Analyse et conception1 semaine
Développement du backend2 semaines
Développement de l’interface2 semaines
Tests et corrections1 semaine
Déploiement et documentation1 semaine
6.2 Livrables
Code source complet du projet.
Documentation technique et utilisateur.Maquettes des interfaces (wireframes ou prototypes).
Fichier README détaillant les instructions d’installation et de déploiement.
