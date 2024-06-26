# Module d'énumération

## Description

Ce module est conçu pour extraire diverses informations sur un fichier binaire en utilisant des commandes système telles que `file`, `checksec`, `strings`, et `ldd`. Il permet d'identifier les fonctions vulnérables, les chaînes imprimées importantes, les bibliothèques dynamiques utilisées, et les protections de sécurité activées.

## Usage

### Fonctions Principales

#### `file_cmd`

Cette fonction exécute la commande `file` sur le fichier binaire et retourne des informations telles que le format, le nombre de bits, le lien et si le fichier est "strippé" ou non.

##### Arguments

- `FILENAME` : Chemin du fichier binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

##### Exemple

```python
file_info = file_cmd("path/to/binary", True)
```

#### `checksec_cmd`

Cette fonction exécute la commande `checksec` pour obtenir des informations sur les protections de sécurité activées sur le fichier binaire.

##### Arguments

- `FILENAME` : Chemin du fichier binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

##### Exemple

```python
checksec_info = checksec_cmd("path/to/binary", True)
```

#### `strings_cmd`

Cette fonction exécute la commande `strings` pour extraire les chaînes de caractères imprimées dans le fichier binaire et identifier les fonctions vulnérables.

##### Arguments

- `FILENAME` : Chemin du fichier binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

##### Exemple

```python
strings_info = strings_cmd("path/to/binary", True)
```

#### `ldd_cmd`

Cette fonction exécute la commande `ldd` pour obtenir la liste des bibliothèques dynamiques utilisées par le fichier binaire.

##### Arguments

- `FILENAME` : Chemin du fichier binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

##### Exemple

```python
ldd_info = ldd_cmd("path/to/binary", True)
```

### Fonctionnement du Module

#### Initialisation et Exécution des Commandes

Le module commence par importer les bibliothèques nécessaires et définir les listes de fonctions vulnérables et de chaînes de caractères importantes.

#### Exécution des Commandes

Le module définit des fonctions pour exécuter les commandes `file`, `checksec`, `strings`, et `ldd`, et retourne les informations collectées sous forme de dictionnaires.

#### Gestion des Erreurs

Une fonction `run_command` encapsule l'exécution des commandes avec une gestion des erreurs et met à jour les informations du binaire.

### Fonction Principale

#### `launch_enum_cmd`

Cette fonction principale lance toutes les commandes d'énumération sur le fichier binaire et rassemble les résultats.

##### Arguments

- `TARGET_FILE_PATH` : Chemin du fichier binaire cible.
- `binary_info` : Dictionnaire contenant les informations du binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.