import os
import re

def replace_in_file(file_path, old_pattern, new_pattern):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Perform the replacement
    content = re.sub(old_pattern, new_pattern, content)
    
    with open(file_path, 'w') as file:
        file.write(content)

def process_files_in_folder(old_pattern, new_pattern):
    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        if file_name.endswith('.html'):
            file_path = os.path.join(current_directory, file_name)
            replace_in_file(file_path, old_pattern, new_pattern)

def main():
    old_pattern = r'<h3 class="f2 lh-solid sans-serif">(.*?)</h3>'
    new_pattern = r'<h2>\1</h2>'
    process_files_in_folder(old_pattern, new_pattern)

if __name__ == "__main__":
    main()
