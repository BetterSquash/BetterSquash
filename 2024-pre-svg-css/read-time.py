import os
import re
from bs4 import BeautifulSoup

def estimate_reading_time(text):
    words_per_minute = 200
    words = text.split()
    num_words = len(words)
    read_time_minutes = max(1, round(num_words / words_per_minute))
    return read_time_minutes

def update_read_time_in_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Extract body content, ignoring header and footer for reading time calculation
    body = soup.body
    if not body:
        return

    # Temporarily remove header and footer from the body content
    headers = body.find_all('header')
    footers = body.find_all('footer')
    for tag in headers + footers:
        tag.extract()

    text = body.get_text(separator=' ', strip=True)
    estimated_time = estimate_reading_time(text)
    read_time_str = f"{estimated_time}-Min Read"

    # Restore header and footer in their original positions
    for header in headers:
        body.insert(0, header)
    for footer in footers:
        body.append(footer)

    # Search for "X-Min Read" and replace it with the estimated read time
    for tag in soup.find_all(string=re.compile(r"\d+-Min Read")):
        old_text = tag
        new_text = re.sub(r"\d+-Min Read", read_time_str, old_text)
        tag.replace_with(new_text)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    return estimated_time

def process_html_files(directory):
    changes_made = []

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            estimated_time = update_read_time_in_html(file_path)
            if estimated_time is not None:
                changes_made.append((filename, estimated_time))

    with open(os.path.join(directory, 'ReadTimeChanges.txt'), 'w', encoding='utf-8') as log_file:
        for filename, estimated_time in changes_made:
            log_file.write(f"{filename}: {estimated_time}-Min Read\n")

# Specify the directory containing HTML files
directory = os.path.dirname(os.path.abspath(__file__))
process_html_files(directory)
