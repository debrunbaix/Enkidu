# Module d'Analyse IA

## Description

Ce module utilise l'API d'OpenAI pour améliorer la lisibilité et la compréhension du pseudo code C généré par Ghidra. Il renomme les variables pour qu'elles soient plus logiques et compréhensibles, et fournit une description détaillée du code, y compris les problèmes de sécurité potentiels.

## Pré-requis

Assurez-vous de placer votre clé API OpenAI dans un fichier `.env` à la racine de votre projet :

```
OPENAI_API_KEY=APIKEY
```

## Fonctionnement Global

### Étape 1 : Récupération de la clé API OpenAI

La fonction `get_openai_api_key` charge le fichier `.env` et récupère la clé API OpenAI. Cette clé est nécessaire pour effectuer des requêtes à l'API OpenAI.

```python
def get_openai_api_key():
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    output('+', 1, 'OpenAI API key retrieved successfully.')
    return OPENAI_API_KEY
```

### Étape 2 : Analyse du Code avec l'API OpenAI

La fonction `gpt_analyse` envoie le pseudo code C à l'API OpenAI pour renommer les variables et fournir une description du code. Elle lit le contenu du fichier de désassemblage, crée un prompt et envoie une requête à l'API OpenAI.

```python
def gpt_analyse(function, OPENAI_API_KEY, DISASSEMBLY_CODE_PATH, client, VERBOSE):
    file_path = os.path.join(DISASSEMBLY_CODE_PATH, function)
    with open(file_path, 'r') as file:
        code_content = file.read()
    
    prompt = PROMPT_START + "\n```c\n" + code_content + "\n```"
    output("info", 2, f"Sending prompt to OpenAI.") if VERBOSE else None
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI language model."},
            {"role": "user", "content": prompt},
        ]
    )
    output("info", 2, f"Getting response from OpenAI.") if VERBOSE else None

    response_content = response.choices[0].message.content
    code, description = response_content.split('```\n\n', 1)
    code = code.replace('```c\n', '').strip()
    description = description.strip()
    
    output("info", 2, f"Response from OpenAI parsed.") if VERBOSE else None
    return {
        "code": code, 
        "description": description
    }
```

### Étape 3 : Formatage de la Description

La fonction `format_gpt_description` nettoie la description générée par l'API OpenAI en remplaçant les balises Markdown.

```python
def format_gpt_description(object):
    object['description'] = object['description'].replace('`', '**')
    return object
```

### Étape 4 : Conversion du Pseudo Code en Code Lisible

La fonction `pseudoC_to_readableC` gère l'analyse complète en appelant les fonctions définies précédemment. Elle récupère la clé API, initialise le client OpenAI, puis analyse chaque fonction du pseudo code C.

```python
def pseudoC_to_readableC(pseudoC, DISASSEMBLY_CODE_PATH, VERBOSE):
    output('+', 0, 'Performing ChatGPT analysis:')
    OPENAI_API_KEY = get_openai_api_key()
    client = OpenAI(api_key=OPENAI_API_KEY)
    result = {}

    for function in pseudoC:
        output("+", 1, f"Requesting analysis for function {function}")
        result[function] = gpt_analyse(function, OPENAI_API_KEY, DISASSEMBLY_CODE_PATH, client, VERBOSE)
        result[function] = format_gpt_description(result[function])

    return result
```

## Arguments

- `pseudoC` : Dictionnaire contenant le pseudo code C à analyser.
- `DISASSEMBLY_CODE_PATH` : Chemin vers le dossier contenant les fichiers de désassemblage.
- `VERBOSE` : Affiche des informations supplémentaires si activé.