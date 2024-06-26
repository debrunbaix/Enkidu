# Fichier main.py

## Description

Le script main sert d'élément central à `Enkidu`, il execute chaque module et gère les arguments de l'outil.

## Usage

### Arguments

- `-t` ou `--target` : Chemin du fichier binaire cible (obligatoire).
- `-v` ou `--verbose` : Active le mode verbeux pour afficher plus d'informations durant l'exécution (optionnel).
- `-ai` ou `--aiAssist` : Utilise l'API de ChatGPT pour améliorer la compréhension des résultats (optionnel).

### Exemple de commande

Pour activer la verbosité et l'assistance IA sur l'analyse, utiliser cette commande :

```bash
python main.py -t chemin/vers/binaire -v -ai
```

Pour faire une execution basique, utiliser ceci :

```bash
python main.py -t chemin/vers/binaire -v -ai
```

## Fonctionnement du script

### Initialisation et Analyse des Arguments

Le script commence par importer les bibliothèques nécessaires et analyser les arguments de la ligne de commande :

```python
parser = argparse.ArgumentParser(description='Target File')
parser.add_argument('-t', '--target', type=str, required=True, help='Mettre un binaire en input.')
parser.add_argument('-v', '--verbose', action='store_true', required=False, help='Affiche plus d\'informations sur l\'execution en cours.')
parser.add_argument('-ai', '--aiAssist', action='store_true', required=False, help='Permet d\'améliorer la compréhension des résultats grâce à l\'API de ChatGPT.')
args = parser.parse_args()
```

### Déclarations des Constantes

Les arguments sont ensuite stockés dans des variables pour une utilisation ultérieure :

```python
VERBOSE = args.verbose
AI_ASSIST = args.aiAssist
TARGET_FILE_PATH = args.target
BINARY_NAME = (TARGET_FILE_PATH.split('/'))[-1]
TODAY_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
REPORT_FOLDER_OUPUT = f"{BINARY_NAME}_report_{TODAY_DATE}"
DISASSEMBLY_CODE_PATH = f"{REPORT_FOLDER_OUPUT}/disassembly_code"
```

### Fonction Principale

La fonction principale du script gère les étapes suivantes :

1. **Ouverture du fichier binaire** : Le script tente d'ouvrir le fichier binaire spécifié et affiche un message de succès ou d'échec.

2. **Création des dossiers de rapport** : Si les dossiers de rapport n'existent pas, ils sont créés.

3. **Phase d'énumération** : La fonction `launch_enum_cmd` est appelée pour effectuer l'énumération du binaire.

4. **Analyse du code source** : Le script analyse le binaire en utilisant la fonction `analyse` et obtient le code de désassemblage via `get_disassembly_code`.

5. **Test de fuzzing et d'exploit** : Les fonctions `fuzztest` et `exploit_test` sont appelées pour tester les vulnérabilités du binaire.

6. **Assistance AI (optionnel)** : Si l'option AI Assist est activée, la fonction `pseudoC_to_readableC` est utilisée pour améliorer la lisibilité du code désassemblé.

7. **Génération du rapport** : Enfin, la fonction `generate_report` génère un rapport détaillé des résultats obtenus.