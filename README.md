# P4_GARRIGOUX_Lucile
Application de gestion pour un club d'échec

## FONCTIONNALITES

Cet outil permet de gérer des tournois d'échecs selon la méthode des tournois suisses.

Il permet de lancer un tournoi de 4 rounds pour 8 joueurs. Il est possible de l'interrompre et reprendre un tournoi après coup.

Il gère une base de donnée de joueurs et de tournois passés.


## Installation

(Optionnel) Installer un environnement virtuel

Si désiré, vous pouvez installer un environnement virtuel pour faire fonctionner le programme. Tout d'abord, utilisez la console pour naviguer vers le dossier où vous voulez lancer votre environnement virtuel (ainsi que l'application) et tapez la commande suivante :

python -m venv ./venv

Puis activez votre environnement virtuel en tapant la commande suivante :

**Pour Windows :**
> .\Scripts\activate.bat

**Pour Max ou Linux :**
> source ./bin/activate

Vous constaterez que le préfixe de votre ligne de commande a changé, par exemple comme ceci :

> C:\Users\LG\Documents\Projet 4> venv\Scripts\activate

> (scraper) C:\Users\LG\Projet 4>

Votre environnement virtuel est maintenant activé. Toute installation de paquet se fera dans cet environnement.

## Installer les paquets nécessaires

Pour installer les paquets nécessaires, utilisez la console pour naviguer jusqu'au dossier où vous avez téléchargé l'application et son document requirement.txt. Tapez les instructions suivantes dans la console :

> pip install -r requirements.txt

Pip installera alors les paquets nécessaires.

## Usage
Une fois l'installation finie, naviguez jusqu'au dossier où vous avez installé l'application. Vous pouvez alors la lancer en tapant la commande suivante dans la console :

**Pour Mac ou Windows :**
> main.py

**Pour Linux :**
> ./main

## Vérifier l'intégrité du code
Pour générer un rapport flake8 sur l'intégrité du code, entrez la commande suivante :

> flake8 chemin\vers\le\dossier\de\l'application --format=html --htmldir=flake-report

Veuillez noter que le fichier requirement doit déjà avoir été installé.
