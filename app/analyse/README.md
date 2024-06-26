# Module d'analyse

## Description

Ce module est conçu pour analyser un fichier binaire ELF en extrayant ses sections, son code assembleur, et les sections de données en lecture seule (.rodata). Il utilise la bibliothèque `pyelftools` pour traiter les fichiers ELF et `capstone` pour la désassemblage du code.

## Usage

### Fonctions Principales

#### `get_elf_binary_sections`

Cette fonction parcourt les sections d'un fichier ELF et met à jour un dictionnaire avec les adresses et les noms des sections.

##### Arguments

- `elffile` : Objet ELFFile représentant le fichier binaire.
- `sections` : Dictionnaire des sections du binaire.

#### `analyse`

Cette fonction principale du module analyse le fichier binaire en extrayant les sections, le code assembleur et les sections de données en lecture seule (.rodata).

##### Arguments

- `info` : Dictionnaire contenant des informations sur le binaire.
- `binary` : Fichier binaire ouvert.
- `VERBOSE` : Affiche des informations supplémentaires si activé.

### Fonctionnement du Module

#### Initialisation et Extraction des Sections

Le module commence par importer les bibliothèques nécessaires et définir les fonctions pour extraire les sections ELF et analyser le binaire.

#### Extraction du Code Assembleur

La fonction `get_assembly_code` utilise `capstone` pour désassembler le code de la section .text d'un fichier ELF.

#### Extraction des Sections de Données en Lecture Seule

La fonction `get_rodata` extrait les chaînes de caractères de la section .rodata d'un fichier ELF.

### Dépendances

Le module dépend des bibliothèques suivantes :

- `pyelftools`
- `capstone`

## Fichiers Sources

### `analyse.py`

Contient la fonction principale `analyse` et la fonction `get_elf_binary_sections`.

### `assembly.py`

Contient les fonctions pour désassembler le code de la section .text.

#### Fonctions

- `save_assembly_to_file` : Sauvegarde le code assembleur dans un fichier.
- `get_assembly_code` : Désassemble le code de la section .text.

### `get_src_code.py`

Contient des fonctions pour extraire le code source et les sections de données en lecture seule (.rodata).

#### Fonctions

- `get_elf_binary_sections` : Extrait les sections ELF.
- `get_assembly` : Désassemble le code de la section .text.
- `get_rodata_sections` : Extrait les chaînes de caractères de la section .rodata.
- `get_relocations` : Extrait les informations de relocation.
- `save_assembly_to_file` : Sauvegarde le code assembleur dans un fichier.

### `sections.py`

Contient les fonctions pour extraire les sections de données (.bss, .data, .rodata) d'un fichier ELF.

#### Fonctions

- `get_bss` : Extrait la section .bss.
- `get_data` : Extrait la section .data.
- `get_rodata` : Extrait la section .rodata.