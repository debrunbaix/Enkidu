from app.output_functions import output
from openai import OpenAI
import dotenv
import os

PROMPT_START = """i
J'ai le pseudo code C suivant généré par Ghidra. Pouvez-vous changer les noms de variables afin qu'ils soient plus logiques et compréhensibles ? Ensuite, fournissez-moi le nouveau code ainsi qu'un paragraphe expliquant ce que fait le code, l'output attendue est nouveau code avec nom de variable changé et ensuite le paragraphe explicatif (qui ne dois avoir aucune syntaxe pour embélir sur chacun des mots, le texte doit être brut et en anglais) mais rien d'autre.
"""

#
# Function to get the OpenAI API key from the .env file
#
def get_openai_api_key():
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    output('+', 1, 'Getting API key done.')
    return OPENAI_API_KEY
#
# Function to request OpenAI's API to get better name varaible and description of code
#
def gpt_analyse(function, OPENAI_API_KEY, DISASSEMBLY_CODE_PATH, client):
    file_path = os.path.join(DISASSEMBLY_CODE_PATH, function)
    with open(file_path, 'r') as file:
        code_content = file.read()
    
    prompt = PROMPT_START + "\n```c\n" + code_content + "\n```"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI language model."},
            {"role": "user", "content": prompt},
        ]
    )

    response_content = response.choices[0].message.content
    code, description = response_content.split('```\n\n', 1)
    code = code.replace('```c\n', '').strip()
    description = description.strip()

    return {
        "code": code, 
        "description": description
    }

def pseudoC_to_readableC(pseudoC, DISASSEMBLY_CODE_PATH):
    output('+', 0, 'ChatGPT Analysis.')
    OPENAI_API_KEY = get_openai_api_key()
    client = OpenAI(api_key=OPENAI_API_KEY)
    result = {}

    for function in pseudoC:
        print(function)
        result[function] = gpt_analyse(function, OPENAI_API_KEY, DISASSEMBLY_CODE_PATH, client)

    return result
