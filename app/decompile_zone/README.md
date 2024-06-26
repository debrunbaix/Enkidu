# Module de décompilation

## Description

Ce module est conçu pour décompiler un fichier binaire en utilisant Ghidra en mode headless. Il permet d'extraire et de filtrer les fonctions décompilées afin d'obtenir un pseudocode lisible. Le module inclut la vérification des chemins de projet et la gestion des commandes de décompilation.

## Usage

### Fonctions Principales

#### `vrfy_path`

Cette fonction vérifie si un projet Ghidra existe déjà et le supprime s'il existe.

##### Arguments

- `path` : Chemin du projet Ghidra.
- `BINARY_NAME` : Nom du binaire.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

#### `get_disassembly_code`

Cette fonction principale du module exécute Ghidra en mode headless pour décompiler un fichier binaire et filtre les fonctions décompilées.

##### Arguments

- `BINARY_NAME` : Nom du fichier binaire.
- `TARGET_FILE_PATH` : Chemin du fichier binaire cible.
- `DISASSEMBLY_CODE_PATH` : Chemin pour sauvegarder le code décompilé.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

### Fonctionnement du Module

#### Initialisation et Vérification des Chemins

Le module commence par importer les bibliothèques nécessaires et définir les fonctions pour vérifier et gérer les projets Ghidra.

#### Exécution de la Décompilation

La fonction `get_disassembly_code` exécute Ghidra en mode headless avec les paramètres appropriés pour décompiler le fichier binaire. Les résultats sont ensuite filtrés et sauvegardés.

### Dépendances

Le module dépend de la bibliothèque `subprocess` pour exécuter les commandes système et de `shutil` et `os` pour la gestion des fichiers et des dossiers.

## Fichiers Sources

### `get_disassembly_code.py`

Contient la fonction principale `get_disassembly_code` et la fonction de vérification `vrfy_path`.

#### Fonctions

- `vrfy_path` : Vérifie et supprime les projets Ghidra existants.
- `get_disassembly_code` : Exécute la décompilation et filtre les fonctions décompilées.

### `function_filter.py`

Contient les fonctions pour filtrer les fonctions standard C et les fonctions sans `return`.

#### Fonctions

- `find_no_return_function` : Vérifie si une fonction contient une instruction `return`.
- `function_filter` : Filtre les fonctions standard C et les fonctions sans `return`.