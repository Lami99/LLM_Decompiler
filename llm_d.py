import os
import sys
from openai import OpenAI

# Check if the script was run with a filename argument
if len(sys.argv) < 2:
    print("Usage: llm_d.py <input_file_name>")
    exit()

filename = sys.argv[1]

# Replace the placeholder with your actual OpenAI API key
OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

# Construct the output file name
output_file_name = f"{os.path.splitext(filename)[0]}_vulnerabilities.txt"

# Check if the input file exists and read its content
if os.path.exists(filename):
    with open(filename, 'r') as file:
        code = file.read()
else:
    print("File does not exist.")
    exit()

# Construct the prompt
prompt = f"""
As a highly skilled static code analyzer for C code, you're tasked with examining the provided decompiled source code, originally written in C. The code has potentially gone through multiple rounds of filtering and reconstruction to enhance context awareness, as the original executable was stripped.

Please perform a thorough analysis, taking into account that some artifacts may be introduced by the enhancements from another language model. Ignore any vulnerabilities that seem to arise due to these enhancements and filtering processes.

Your analysis should only include vulnerabilities that you can confirm with certainty. Any uncertain or potential vulnerabilities should be cataloged separately.
Act such that false negative is much much better than false positives, ie really avoid annoncing any vulnerability unless it is 100% confirmed
you are not expected to always annonce the presence of vulnerabilities, you will encounter situations where you are given the code of a bug after it was fixed, be conservatif and only annonce when it is obivious the presence of the bug


Output Format:
- Confirmed Vulnerabilities: List each confirmed vulnerability along with the line number where it occurs.
- Potential Vulnerabilities: List each potential or doubtful vulnerability along with the line number, separated from the confirmed issues.

Source Code:
{code}

Provide the results as follows:
Confirmed_vulnerabilities : list
Potential_vulnerabilities : list
"""
# Send the request to the ChatGPT API
response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": prompt}
  ]
)

response_text = response.choices[0].message.content

# Save the response to the output file
with open(output_file_name, 'w') as output_file:
    output_file.write(response_text)

print(f"Analysis saved to {output_file_name}")
