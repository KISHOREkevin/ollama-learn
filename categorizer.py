import os
import sys

import ollama

model = "llama3.2:1b"

input_file = "./data/grocery.txt"
output_file = "./data/catogorized-grocery.txt"


if not os.path.exists(input_file):
    print(f"Error : Input file {input_file} not found")
    sys.exit(1)


with open(input_file, "r") as f:
    items = f.read().strip()


prompt = """
You are an assistant that categorizes and sorts grocery items.

Here is the list of items

{items}

Please:
1. Categorize these items into appropriate categories such as Produce, Diary, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category
3. Present the categorized list in  a clear and organized manner, using bullet points or numbering.
"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
    print(f"Catgorized grocery list has been saved to '{output_file}'")
except Exception as e:
    print(f"Error : {str(e)}")
