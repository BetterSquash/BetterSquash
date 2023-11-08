import os
import re

folder_path = "/Users/phillipmarlowe/Documents/GitHub/2022"  # Replace with the actual path to your HTML files folder

def process_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        match = re.search(r'<meta name="description" content="([^"]+)">', content)
        if match:
            description_content = match.group(1)
            modified_content = re.sub(r'<meta property="og:description" content="[^"]+">', lambda x: x.group().replace('meta property="og:description" content="', f'meta property="og:description" content="{description_content}"'), content)
            with open(file_path, "w") as file:
                file.write(modified_content)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            process_file(file_path)