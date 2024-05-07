import os
import sys
from openai import OpenAI

# Setup OpenAI API client
OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)

def filter_source_code(file_path):
    """
    Read the entire source code from the given file, filter out irrelevant functions using GPT,
    and save the filtered code to a new file.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    # Read the source code from the file
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Construct the prompt for the GPT model
    prompt = f"""
    Given the following decompiled source code, remove any empty functions, functions that seem like standard library imports, and keep only functions that have substantial logic. Here is the decompiled source code:

    {source_code}

    Please return only the relevant functions that contain concrete logic code, THE FULL FUNCTION with its code, not only its name
    """

    try:
        # Send the prompt to the GPT model
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        filtered_code = response.choices[0].message.content

        # Save the filtered code to a new file
        output_filename = f"{os.path.splitext(file_path)[0]}_filtered.c"
        with open(output_filename, "w") as output_file:
            output_file.write(filtered_code)

        print(f"Filtered code saved to {output_filename}")

    except Exception as e:
        print(f"Error during API call or processing: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_decompiled_source_code>")
        sys.exit(1)
    filter_source_code(sys.argv[1])
