from openai import OpenAI
from dotenv import load_dotenv
import os

# Load your OpenAI key from an environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def categorize_ctf_and_provide_hints(vulnerability_report, enhanced_decompiled_code):
    prompt = f"""
    Based on the following vulnerability report and enhanced decompiled code, determine the category of the CTF challenge. Provide brief hints, relevant sources, webpages, and references to old CTF challenges that could help in solving this challenge. Be brief and convenient for a CTF player to quickly find relevant information.

    Vulnerability Report:
    {vulnerability_report}

    Enhanced Decompiled Code:
    {enhanced_decompiled_code}

    CTF Category, Hints, and Resources:
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    ctf_info = response.choices[0].message.content
    return ctf_info

def main(vulnerability_report_file, enhanced_decompiled_file, output_file):
    with open(vulnerability_report_file, 'r') as f:
        vulnerability_report = f.read()

    with open(enhanced_decompiled_file, 'r') as f:
        enhanced_decompiled_code = f.read()

    ctf_info = categorize_ctf_and_provide_hints(vulnerability_report, enhanced_decompiled_code)

    with open(output_file, 'w') as f:
        f.write(ctf_info)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Determine the CTF challenge category and provide hints and resources.")
    parser.add_argument("enhanced_decompiled_file", help="Path to the enhanced decompiled code file.")
    parser.add_argument("vulnerability_report_file", help="Path to the vulnerability report file.")
    parser.add_argument("output_file", help="Path to the output file for the CTF hints and resources.")

    args = parser.parse_args()
    main(args.vulnerability_report_file, args.enhanced_decompiled_file, args.output_file)
