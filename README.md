# P4_GARRIGOUX_Lucile
Management application for a chess tournament. French and English version available.

La documentation en français est disponible plus bas dans le ReadMe.

## ENGLISH - Introduction

This application helps managing a chess tournament according to the Swiss method.

It allows the user to launch a 4-rounds tournament for 8 participants, automatically matching players according to their rankings. You can stop the application at any time during the tournament and resume later.

You can consult the database whenever you wish to see players profiles and past tournaments.


## Installation

#(Optional) Virtual environment installation

You can install a virtual environment so as to keep any library installation contained in it. First, navigate with the command line up to the folder where you want to keep your virtual environment. Type the following command:

> python -m venv venv

Then activate your virtual environment by typing the following:

**For Windows :**
> venv\Scripts\activate

**For Max or Linux :**
> source .venv/bin/activate

You will see that that the prefix on your console has changed, for instance like below:

> C:\Users\LucileGB\Document\Projet 4>

> (venv) C:\Users\LucileGB\Document\Projet 4>

You are now in your virtual environment. To deactivate it once you're done running the app, just type deactivate.

# Install the relevant libraries

To install the necessary libraries, use the command line to navigate in the application folder and type the following:

> pip install -r requirements.txt

## Usage
Once the installation is finished, navigate to the folder and launch the application by typing the following in the command line:

**For Mac or Windows :**
> main.py

**For Linux :**
> ./main

## Run linting report
To generate a flake8 report on code cleanliness, enter the following command:

> flake8 chemin\vers\le\dossier\de\l'application --format=html --htmldir=flake-report

Please note that the content of requirements.txt must have already been installed.


## FRANCAIS - Présentation

Cet outil permet de gérer des tournois d'échecs selon la méthode des tournois suisses.

Il permet de lancer un tournoi de 4 rounds pour 8 joueurs, en appariant automatiquement les joueurs à chaque round selon leur classement. Il est possible d'interrompre le programme à mi-tournoi et de reprendre ultérieurement.

Il est possible à tout moment de consulter la base de données, qui liste les joueurs et les tournois passés.

## Installation

#(Optionnel) Installer un environnement virtuel

Vous pouvez installer un environnement virtuel afin d'y cantonner toute installation de paquet. Tout d'abord, utilisez la console pour naviguer vers le dossier où vous voulez lancer votre environnement virtuel et tapez la commande suivante :

> python -m venv venv

Puis activez votre environnement virtuel en tapant la commande suivante :

**Pour Windows :**
> venv\Scripts\activate

**Pour Max ou Linux :**
> source .venv/bin/activate

Vous constaterez que le préfixe de votre ligne de commande a changé, par exemple comme ceci :

> C:\Users\LucileGB\Document\Projet 4>

> (venv) C:\Users\LucileGB\Document\Projet 4>

Vous êtes maintenant dans votre environnement virtuel. Pour le désactiver, tapez simplement "deactivate" dans la console.

# Installer les paquets nécessaires

Pour installer les paquets nécessaires, utilisez la console pour naviguer dans le dossier de l'application et tapez l'instruction suivante :

> pip install -r requirements.txt

Pip installera alors les paquets nécessaires.

## Usage
Une fois l'installation finie, naviguez jusqu'au dossier où vous avez installé l'application. Vous pouvez alors la lancer en tapant la commande suivante dans la console :

**Pour Mac ou Windows :**
> main.py

**Pour Linux :**
> ./main

## Générer un rapport sur la qualité du code
Pour générer un rapport flake8, entrez la commande suivante :

> flake8 chemin\vers\le\dossier\de\l'application --format=html --htmldir=flake-report

Veuillez noter que le contenu de requirements.txt doit déjà avoir été installé.
