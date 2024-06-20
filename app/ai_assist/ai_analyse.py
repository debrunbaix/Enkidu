from app.output_functions import output
from openai import OpenAI
import dotenv
import os

PROMPT_START = """
Je vous fournis un pseudo code C généré avec Ghidra. Veuillez changer les noms des variables pour qu'ils soient plus logiques et compréhensibles. L'output doit être que en Anglais et inclure deux parties: Le code changé et ensuite Un paragraphe explicatif du code, qui évoque aussi en détail les problèmes de sécurité des fonctions. Le paragraphe doit rester brut, sans style, sans guillemets ou autres balises Markdown.
"""

#
# Function to get the OpenAI API key from the .env file
#
def get_openai_api_key():
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    output('+', 1, 'OpenAI API key retrieved successfully.')
    return OPENAI_API_KEY
#
# Function to request OpenAI's API to get better name varaible and description of code
#
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

#
# Function to format the GPT description output to delete markdown syntaxe
#
def format_gpt_description(object):
    object['description'] = object['description'].replace('`', '**')
    return object

def pseudoC_to_readableC(pseudoC, DISASSEMBLY_CODE_PATH, VERBOSE):
    output('+', 0, 'Performing ChatGPT analysis:')
    OPENAI_API_KEY = get_openai_api_key()
    client = OpenAI(api_key=OPENAI_API_KEY)
    result = {}

    for function in pseudoC:
        output("+", 1, f"Requesting analysis for function {function}")
        result[function] = gpt_analyse(function, OPENAI_API_KEY, DISASSEMBLY_CODE_PATH, client, VERBOSE)
        result[function] =  format_gpt_description(result[function])

    return result
