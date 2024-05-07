import os
import json
import sys
from openai import OpenAI

# Constants for the function markers
FUNCTION_START_MARKER = "----- START OF FUNCTION: {name} -----"
FUNCTION_END_MARKER = "----- END OF FUNCTION: {name} -----"

# Setup OpenAI API client
OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

def send_to_gpt_and_parse(function_data, name_map):
 
    prompt = f"""
    Enhance the readability and maintainability of this C function(the result of decompiling a stripped binary) by adding comments and renaming variables and functions to be more descriptive. Your task includes two main parts:

    1. Analyze the provided C function code for readability improvements.
    2. Update any internal function calls using the provided name map to ensure all references are consistent with previously enhanced functions.

    Function Signature:
    {function_data['signature']}

    Original Function Code:
    {function_data['body']}

    Current Name Map for Reference (Use this to update internal function calls):
    {json.dumps(name_map, indent=2)}

    Instructions:
    - If the function contains calls to other functions that appear in the name map, replace these calls with the new names from the map.
    - Decide on a new descriptive name for the function you're currently enhancing, if necessary. Add this new name as a key-value pair in your response.
    - Avoid renaming or modifying standard library functions or their calls; focus only on user-defined functions and logic.
    - Ensure your response strictly follows the below format, containing only the necessary structured information with no additional comments or verbose explanations.

    Expected Response Format:
    new_map_pair: old_function_name : new_descriptive_function_name
    enhanced_code:
    // New Function Signature: [optional if changed]
    [Enhanced code here]

    Note: Ensure that the enhanced code does not change the core logic or behavior of the original code. The goal is to improve code clarity and maintainability without altering functionality.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        output_text = response.choices[0].message.content
        print(output_text)
        
        # Parsing the expected structured output
        lines = output_text.split('\n')
        new_map_pair_line = lines[0]
        enhanced_code = '\n'.join(lines[1:])  # Assuming all lines after the first are code

        # Parsing the new map pair
        map_pair_prefix = "new_map_pair: "
        if new_map_pair_line.startswith(map_pair_prefix):
            map_content = new_map_pair_line[len(map_pair_prefix):]
            old_name, new_name = map_content.split(' : ')
            name_map.update({old_name: new_name})

        return enhanced_code

    except Exception as e:
        print(f"Error during API call or processing: {str(e)}")
        return function_data['body']  # Fallback to original body in case of failure

def process_json_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)

    with open(file_path, 'r') as file:
        functions = json.load(file)

    name_map = {}
    enhanced_code_blocks = []

    for function_data in functions:
        enhanced_code = send_to_gpt_and_parse(function_data, name_map)
        enhanced_code_blocks.append(f"// Function: {function_data['name']}\n{function_data['signature']}\n{enhanced_code}\n")
        print(name_map)
    # Save the enhanced functions to a new source code file
    output_filename = f"{os.path.splitext(file_path)[0]}_enhanced.c"
    with open(output_filename, "w") as output_file:
        output_file.write("\n\n".join(enhanced_code_blocks))

    print(f"Enhanced code saved to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_decompiled_output_json>")
        sys.exit(1)
    process_json_file(sys.argv[1])