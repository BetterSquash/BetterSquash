import os
from bs4 import BeautifulSoup

def scan_directory(directory):
    missing_twitter_desc = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                soup = BeautifulSoup(content, 'html.parser')
                
                twitter_description = soup.find('meta', attrs={'name': 'twitter:description'})
                
                if not twitter_description:
                    missing_twitter_desc.append(file)
    
    return missing_twitter_desc

def main():
    current_directory = os.getcwd()
    missing_files = scan_directory(current_directory)
    
    with open('Missing_Twitter_Description.txt', 'w', encoding='utf-8') as f:
        for filename in missing_files:
            f.write(f"{filename}\n")

if __name__ == "__main__":
    main()