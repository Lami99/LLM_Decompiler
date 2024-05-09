import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

if len(sys.argv) < 2:
    print("Usage: llm_r.py <decompiled_code_file>")
    sys.exit()

input_filename = sys.argv[1]

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

output_filename = f"{os.path.splitext(input_filename)[0]}_enhanced.c"

if os.path.exists(input_filename):
    with open(input_filename, 'r') as file:
        decompiled_code = file.read()
else:
    print("Decompiled code file does not exist.")
    sys.exit()

# Constructing a detailed prompt for GPT
prompt = """\
Please focus on the following decompiled C code from a user's program: 
1. Add comments before each function and inside functions to explain what the code is doing, especially if the instructions are unclear or complex.
2. Rename variables and functions to names that are more representative of their purpose or functionality. Ensure the changes make the code clearer without altering its logic, semantics, or the actual instructions, as it will be analyzed for vulnerabilities later.
The goal is to enhance readability and maintainability of the code without changing its underlying behavior. The result of this prompt, will directly be pasted inside a .c file and sent again to another LLM for vulnerability detection

Decompiled code:
"""

prompt += decompiled_code

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": prompt}
  ]
)

enhanced_code = response.choices[0].message.content

# Save the enhanced code to the output file
with open(output_filename, 'w') as output_file:
    output_file.write(enhanced_code)

print(f"Enhanced code saved to {output_filename}")
