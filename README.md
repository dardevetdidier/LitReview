# LitRewiew : Application de partage de critiques de livres ou d'articles

LItReview est une application web permettant à une communauté de passionnés de lecture de demander, rédiger et partager des critiques de livres ou d'articles. 

LitReview est actuellemnt en version 'Produit Viable Minimum' et ne reflète donc pas la totalité des fonctionnalités de la version définitive.
____________________________

### TECHNOLOGIES 
* Python 3.9.2
* Django 3.2.6
* Bootstrap 5
* html /css

### INSTALLATION

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/dardevetdidier/LitReview.git`.  


2. Depuis un terminal, rendez-vous à la racine du répertoire LitReview avec la commande `$ cd LitReview`.


3. Créer un environnement virtuel pour le projet avec `$ python -m venv venv`.


4. Activer l'environnement virtuel avec `$ venv/Scripts/activate` sous windows ou `$ source venv/bin/activate` sous MacOs ou Linux.

5. installer les dépendances du projet avec la commande `$ pip install -r requirements.txt`.


### DEMARRER LE SERVEUR ET OUVRIR L'APPLICATION

1. Pour lancer le serveur, depuis le répertoire racine du projet, utiliser la commande `$ python manage.py runserver`


2. Lancer l'application dans un navigateur en accédant à l'url : [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### FONCTIONALITES 

Pour une première utilisation vous devez créer un compte. Pour cela, cliquez sur "S'inscrire" depuis la page d'accueil puis remplissez les champs du formulaire.

Une fois enregistré, l'utilisateur doit se connecter depuis la page d'accueil avec son nom d'utilisateur et son mot de passe, créés lors de l'inscription.

Une fois connecté l'utilisateur peut :
* Consulter le flux de posts de tous les utilisateurs (Flux)
* Créer un ticket (demande de critique)
* Créer une critique. Pour cela il créera un ticket et y répondra dans un seul formulaire de création
* Répondre à un ticket posté par un autre utilisateur ou par lui-même. Un ticket ne peut recevoir qu'une seule réponse
* Consulter ses propres posts (Mes Posts)
* Suivre un autre utilisateur (Abonnements)
* Se déconnecter