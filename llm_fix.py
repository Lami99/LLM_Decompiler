from openai import OpenAI
from dotenv import load_dotenv
import json
import os

# Load your OpenAI key from an environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def suggest_fixes(decompiled_code, vulnerability_report):
    prompt = f"""
    Based on the following decompiled code and vulnerability report, suggest the necessary changes to make the code bug-free. Provide specific changes and a brief explanation for each change.

    Decompiled Code:
    {decompiled_code}

    Vulnerability Report:
    {vulnerability_report}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    fixes = response.choices[0].message.content
    return fixes

def main(decompiled_code_file, vulnerability_report_file, output_file):
    with open(decompiled_code_file, 'r') as f:
        decompiled_code = f.read()

    with open(vulnerability_report_file, 'r') as f:
        vulnerability_report = f.read()

    fixes = suggest_fixes(decompiled_code, vulnerability_report)

    with open(output_file, 'w') as f:
        f.write(fixes)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Suggest fixes for decompiled code based on vulnerability report.")
    parser.add_argument("decompiled_code_file", help="Path to the decompiled code file.")
    parser.add_argument("vulnerability_report_file", help="Path to the vulnerability report file.")
    parser.add_argument("output_file", help="Path to the output file for the suggested fixes.")

    args = parser.parse_args()
    main(args.decompiled_code_file, args.vulnerability_report_file, args.output_file)
