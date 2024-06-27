import os
import re
from bs4 import BeautifulSoup

def get_meta_content(soup, name):
    meta = soup.find('meta', attrs={'name': name})
    return meta['content'] if meta else None

def scan_directory(directory):
    differences = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                soup = BeautifulSoup(content, 'html.parser')
                
                description = get_meta_content(soup, 'description')
                twitter_description = get_meta_content(soup, 'twitter:description')
                
                if description != twitter_description:
                    differences.append(file)
    
    return differences

def main():
    current_directory = os.getcwd()
    differences = scan_directory(current_directory)
    
    with open('Meta_Difference.txt', 'w', encoding='utf-8') as f:
        for filename in differences:
            f.write(f"{filename}\n")

if __name__ == "__main__":
    main()