import os
import dotenv
from openai import OpenAI

from app.output_functions import output

PROMPT_START = """
Je vous fournis un pseudo code C généré avec Ghidra. Veuillez changer les noms des variables pour qu'ils soient plus logiques et compréhensibles. L'output doit être que en Anglais et inclure deux parties: Le code changé et ensuite Un paragraphe explicatif du code, qui évoque aussi en détail les problèmes de sécurité des fonctions. Le paragraphe doit rester brut, sans style, sans guillemets ou autres balises Markdown.
"""

def get_openai_api_key() -> str:
    """
        get api key from .env file
    """
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    output('+', 1, 'OpenAI API key retrieved successfully.')
    return OPENAI_API_KEY

def gpt_analyse(function, DISASSEMBLY_CODE_PATH: str, client, VERBOSE: bool) -> dict:
    """
        request OpenAI's API to get better name varaible and description of code
    """
    file_path = os.path.join(DISASSEMBLY_CODE_PATH, function)
    with open(file_path, 'r', encoding="utf-8") as file:
        code_content = file.read()
    
    prompt = PROMPT_START + "\n```c\n" + code_content + "\n```"
    if VERBOSE:
        output("info", 2, "Sending prompt to OpenAI.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI language model."},
            {"role": "user", "content": prompt},
        ]
    )
    if VERBOSE:
        output("info", 2, "Getting response from OpenAI.")

    response_content = response.choices[0].message.content
    code, description = response_content.split('```\n\n', 1)
    code = code.replace('```c\n', '').strip()
    description = description.strip()
    
    if VERBOSE:
        output("info", 2, "Response from OpenAI parsed.")
    return {
        "code": code, 
        "description": description
    }

def format_gpt_description(pseaudo_code_ai: dict) -> dict:
    """
        format the GPT description output to delete markdown syntaxe
    """
    pseaudo_code_ai['description'] = pseaudo_code_ai['description'].replace('`', '**')
    return pseaudo_code_ai

def pseudoc_to_readablec(pseudoc: dict, DISASSEMBLY_CODE_PATH: str, VERBOSE: bool) -> dict:
    """
        1. Get openai API key
        2. Connect to OpenAI
        3. Change pseudo code c to readable 
        4. Add a description
    """
    output('+', 0, 'Performing ChatGPT analysis:')
    OPENAI_API_KEY = get_openai_api_key()
    client = OpenAI(api_key=OPENAI_API_KEY)
    result = {}

    for function in pseudoc:
        output("+", 1, f"Requesting analysis for function {function}")
        result[function] = gpt_analyse(function, DISASSEMBLY_CODE_PATH, client, VERBOSE)
        result[function] =  format_gpt_description(result[function])

    return result
