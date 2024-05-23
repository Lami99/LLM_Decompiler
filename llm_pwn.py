from openai import OpenAI
from dotenv import load_dotenv
import json
import os

# Load your OpenAI key from an environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_pwn_skeleton(refined_code, vulnerability_report, original_code):
    prompt = f"""
    Based on the following refined decompiled code, vulnerability report, and original decompiled code, generate a skeleton for a PWN script in Python. The script should include comments on steps to be done to finish the proof of concept of the bug found or the exploit, with a text explaining the overall idea behind the attack.

    Refined Decompiled Code:
    {refined_code}

    Vulnerability Report:
    {vulnerability_report}

    Original Decompiled Code:
    {original_code}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ]
)

    pwn_skeleton = response.choices[0].message.content
    return pwn_skeleton

def main(refined_code_file, vulnerability_report_file, original_code_file, output_file):
    with open(refined_code_file, 'r') as f:
        refined_code = f.read()

    with open(vulnerability_report_file, 'r') as f:
        vulnerability_report = f.read()

    with open(original_code_file, 'r') as f:
        original_code = f.read()

    pwn_skeleton = generate_pwn_skeleton(refined_code, vulnerability_report, original_code)

    with open(output_file, 'w') as f:
        f.write(pwn_skeleton)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a PWN script skeleton based on decompiled code and vulnerability report.")
    parser.add_argument("refined_code_file", help="Path to the refined decompiled code file.")
    parser.add_argument("vulnerability_report_file", help="Path to the vulnerability report file.")
    parser.add_argument("original_code_file", help="Path to the original decompiled code file.")
    parser.add_argument("output_file", help="Path to the output file for the PWN script skeleton.")

    args = parser.parse_args()
    main(args.refined_code_file, args.vulnerability_report_file, args.original_code_file, args.output_file)
