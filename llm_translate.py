from openai import OpenAI
from dotenv import load_dotenv
import os

# Load your OpenAI key from an environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def translate_code(c_code, target_language):
    prompt = f"""
    Translate the following C source code to {target_language}:

    C Source Code:
    {c_code}

    Translated Code in {target_language}:
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    translated_code = response.choices[0].message.content
    return translated_code

def main(c_source_file, target_language, output_file):
    with open(c_source_file, 'r') as f:
        c_code = f.read()

    translated_code = translate_code(c_code, target_language)

    with open(output_file, 'w') as f:
        f.write(translated_code)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Translate C source code to another programming language.")
    parser.add_argument("c_source_file", help="Path to the C source code file.")
    parser.add_argument("target_language", help="The target programming language for translation.")
    parser.add_argument("output_file", help="Path to the output file for the translated code.")

    args = parser.parse_args()
    main(args.c_source_file, args.target_language, args.output_file)
