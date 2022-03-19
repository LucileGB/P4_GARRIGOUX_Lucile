# P4_GARRIGOUX_Lucile
Application de gestion pour un club d'échec

## FONCTIONNALITES

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

Votre environnement virtuel est maintenant activé.

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

## Vérifier l'intégrité du code
Pour générer un rapport flake8 sur l'intégrité du code, entrez la commande suivante :

> flake8 chemin\vers\le\dossier\de\l'application --format=html --htmldir=flake-report

Veuillez noter que le fichier requirements.txt doit déjà avoir été installé.
