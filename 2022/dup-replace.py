import os
from bs4 import BeautifulSoup

def remove_duplicates_in_html_files():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Iterate over all files in the script's directory
    for filename in os.listdir(script_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(script_dir, filename)
            with open(filepath, "r") as file:
                html_content = file.read()

            soup = BeautifulSoup(html_content, "html.parser")

            # Find all divs with class 'prevnext'
            prevnext_divs = soup.find_all("div", class_="prevnext")

            # Remove duplicate divs
            seen_divs = set()
            for div in prevnext_divs:
                if str(div) in seen_divs:
                    div.decompose()  # Remove the duplicate div
                else:
                    seen_divs.add(str(div))

            # Replace the content of the file with modified HTML
            with open(filepath, "w") as file:
                file.write(str(soup))

# Call the function to remove duplicates in HTML files within the script's directory
remove_duplicates_in_html_files()
