# Enkidu

![](/attachments/banner.png)

Enkidu est un outil de pentest automatique spécialisé dans l'analyse et l'exploitation de binaires.

---

## Table des matières

1. [Introduction](#introduction)

2. [Fonctionnalités](#fonctionnalités)

3. [Installation](#installation)

4. [Utilisation](#utilisation)

5. [Documentation](#documentation)

6. [Contributions](#contributions)

7. [Licence](#licence)

---

## Introduction

Enkidu est un projet open-source développé dans le cadre d'un projet technique en master de cybersécurité. Ce projet vise à fournir un outil robuste et automatisé pour les tests de pénétration sur des binaires, permettant d'énumérer automatiquement des binaires et de découvrir et exploiter des vulnérabilités.

### Information

Pour la partie enumération du binaire, Enkidu utilise la sortie des commandes :

- `file`

- `checksec`

- `strings`

- `ldd`

Ensuite, Enkidu traite la sortie de chacune de ces commandes afin de l'unifier dans un json qui servira de base pour l'analyse.

Pour obtenir le code assembleur du binaire, Enkidu cherche dans le contenue des sections `.text`, `.rodata` etc.. grâce aux librairies `elftools` & `capstone`. 

Pour l'obtention du pseudo code C, Enkidu utilise `Ghidra` et son scripts `AnalyseHeadless` afin d'executer Ghidra en ligne de commande avec mon script de decompilateur dans `/decompile_zone/script/decompiler.py`.

En ce qui concerne la génération de rapports, Enkidu utilise :

- `markdown` pour convertir le texte formaté en Markdown en HTML. Cela permet une flexibilité dans la rédaction du contenu du rapport, qui peut ensuite être facilement converti en un format web visualisable.

- `WeasyPrint` pour convertir des documents HTML en PDF. Elle joue un rôle crucial dans report.py en transformant le contenu HTML généré à partir de Markdown en un document PDF final, permettant une distribution et un archivage faciles des rapports.
---

## Fonctionnalités

- [x] Enumération d'information binaire :

    - [x] Traitement de la commande `file`.

    - [x] Traitement de la commande `checksec`.

    - [x] Traitement de la commande `strings`:

        - [x] Fonctions.

        - [x] Messages d'erreur/succès.

    - [x] Traitement de la commande `ldd`.

    - [x] Récupération des sections du binaire.

    - [x] Obtention du code assembleur.

- [x] Obtention de pseudo code C.

- [x] Analyse automatique des binaires pour identifier les vulnérabilités :

    - [x] Déterminer les fonctions vulnérables.

    - [x] Analyse des sécurités du binaire.

- [ ] Analyser les outputs grâce à ChatGPT.

- [ ] Tentatives d'exploitation automatiques pour contourner les défenses des binaires.

    - [ ] Fuzztesting des entrées utilisateurs.

        - [x] level 1 : Test avec les strings récupéré avant.

        - [ ] level 2 : fuzztesting avancé.

    - [ ] Tentative d'exploitation binaire.

    - [ ] Tentative d'exploitation de format de chaine.

- [x] Génération de rapport.

    - [x] Rapport en `markdown` fait.

    - [x] Rapport en `HTML/CSS` fait.

    - [x] Rapport `PDF` fait.

- [ ] Interface utilisateur intuitive pour faciliter l'utilisation et l'interprétation des résultats.

- [ ] Prise en charge de différents types de binaires et architectures.

---

## Installation

Pour installer Enkidu, suivez les étapes suivantes :

1. Clonez ce référentiel sur votre machine locale :

```bash

git clone https://github.com/Igaemas/Enkidu.git

```

2. Accédez au répertoire Enkidu :

```bash

cd enkidu

```

3. Installer les dépendances :

```bash
python -m pip install -m requirement.txt

```

---

## Documentation

### Arborescence

```
Enkidu/
├── app/                       # Répertoire principal de l'application
│   ├── analyse/               # Contient des scripts pour l'analyse de binaire
│   │   ├── analyse.py         # Script d'initialisation des analyses
│   │   ├── assembly.py        # Script pour analyser le code assembleur
│   │   ├── sections.py        # Script pour analyser les sections du binaire
│   │   └── __init__.py        
│   ├── enumeration/           # Scripts pour l'énumération des binaires
│   │   ├── enum_cmd.py        # Commandes pour l'énumération
│   │   ├── enum.py            # Script pour lancer l'énumération
│   │   └── __init__.py        
│   ├── __init__.py            
│   ├── main.py                # Point d'entrée principal du projet
│   ├── output_functions.py    # Fonctions pour gérer les sorties (log, affichage)
│   ├── fuzztesting.py         # Script pour le fuzz testing des binaires
│   ├── report.py              # Script pour générer les rapports Markdown, HTML/CSS, PDF
│   ├── styles/                # Dossier pour les fichiers CSS et autres ressources de style
│   │   ├── DejaVuSans.ttf     # Police de caractères pour les rapports
│   │   └── styles.css         # Feuille de style CSS pour les rapports
│   └── testFile/              # Dossier contenant des fichiers de test ou exemples de binaires
├── attachments/               # Dossier pour les fichiers joints ou annexes (si nécessaire)
├── LICENSE                    # Fichier de licence pour le projet
├── login_report_2024-05-15/   # Exemple de rapport généré
├── README.md                  # Fichier Markdown fournissant des informations sur le projet
├── requirements.txt           # Liste des dépendances Python nécessaires
└── venv/                      # Environnement virtuel Python
```

---

## Utilisation

```bash
source venv/bin/activate
python3 -m app.main -t <path_to_binary>
``` 

---

## Contributions

Les contributions sont les bienvenues ! Pour contribuer à Enkidu, veuillez suivre ces étapes :

1. Fork le projet sur GitHub.

2. Créez une nouvelle branche avec une fonctionnalité ou une correction de bug que vous souhaitez apporter.

3. Faites vos modifications et testez-les.

4. Soumettez une demande de tirage avec une description détaillée de vos modifications.

---

## Licence

Ce projet est sous licence [MIT](LICENSE).

---
