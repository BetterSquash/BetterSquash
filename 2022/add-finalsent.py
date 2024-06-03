import os
from bs4 import BeautifulSoup

def add_class_to_final_p():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Iterate over all files in the script's directory
    for filename in os.listdir(script_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(script_dir, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()

            soup = BeautifulSoup(html_content, "html.parser")

            # Find the first div with class 'prevnext'
            prevnext_div = soup.find("div", class_="prevnext")

            if prevnext_div:
                # Find all <p> tags before the prevnext div
                all_p_tags = prevnext_div.find_all_previous("p")

                if all_p_tags:
                    # Get the last <p> tag before the prevnext div
                    last_p = all_p_tags[0]
                    last_p["class"] = last_p.get("class", []) + ["finalsent"]

            # Replace the content of the file with modified HTML
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(str(soup))

# Call the function to add class to the final <p> tag before <div class="prevnext"> in HTML files within the script's directory
add_class_to_final_p()

