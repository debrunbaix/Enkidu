# Enkidu

![](/attachments/banner.png)

Enkidu est un outil de pentest automatique spécialisé dans l'analyse et l'exploitation de binaires.

---

## Table des matières

1. [Introduction](#introduction)

2. [Fonctionnalités](#fonctionnalités)

3. [Installation](#installation)

4. [Utilisation](#utilisation)

5. [Contributions](#contributions)

6. [Licence](#licence)

---

## Introduction

Enkidu est un projet open-source développé dans le cadre d'un projet technique en master de cybersécurité. Inspiré par la figure mythique d'Enkidu, ce projet vise à fournir un outil robuste et automatisé pour les tests de pénétration sur des binaires, permettant aux chercheurs en sécurité de découvrir et d'exploiter des vulnérabilités.

### Information

Pour la partie enumération du binaire, Enkidu utilise la sortie des commandes :

- `file`

- `checksec`

- `strings`

- `ldd`

Ensuite, Enkidu traite la sortie de chacune de ces commandes afin de l'unifier dans un json qui servira de base pour l'analyse.

Pour obtenir le code source du binaire, Enkidu utilise les libraries `elftools` & `capstone`.

---

## Fonctionnalités

- [ ] Enumération d'information binaire :

    - [x] traitement de la commande `file`

    - [x] traitement de la commande `checksec`

    - [x] traitement de la commande `strings`:

        - [x] Fonctions

        - [x] Messages d'erreur/succès

    - [x] traitement de la commande `ldd`

    - [x] Récupération des sections et du code assembleur du binaire

    - [ ] traitement de la commande `objdump`

    - [ ] traitement de la commande `readelf`

- [ ] Analyse automatique des binaires pour identifier les vulnérabilités.

- [ ] Tentatives d'exploitation automatiques pour contourner les défenses des binaires.

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

cd enkidu/app

```

3. Installer les dépendances :

```bash
python -m pip install -m requirement.txt

```

---

## Utilisation

```bash
python main.py <pathToFile>
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
