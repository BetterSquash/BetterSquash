import os
import re
from datetime import datetime

def insert_prev_next_links():
    # Get the current folder path where the script is located
    folder_path = os.path.dirname(os.path.realpath(__file__))

    # Get a sorted list of HTML files based on their names
    html_files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith('.html')],
        key=lambda x: datetime.strptime(x, '%Y%m%d.html')
    )

    for i, file in enumerate(html_files):
        file_path = os.path.join(folder_path, file)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        prev_link = html_files[i - 1] if i > 0 else "prevlink"
        next_link = html_files[i + 1] if i < len(html_files) - 1 else "nextlink"

        prev_next_html = f"""
        <div class="prevnext">
            <div style="float: left">&lt;&lt; <a href="{prev_link}">Previous Article</a></div>
            <div style="float: right"><a href="{next_link}">Next Article</a> &gt;&gt;</div>
            <div style="clear: both;"></div>
        </div>
        """

        # Find the correct position to insert the navigation section
        pattern = re.compile(r'(<p><a href="#top">BACK TO TOP ↑</a></p>\s*<hr class="content"/>)')
        match = pattern.search(content)

        if match:
            insertion_point = match.start(1)
            updated_content = content[:insertion_point] + prev_next_html + '\n' + content[insertion_point:]
        else:
            print(f"Could not find the target insertion point in {file}")
            continue

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

if __name__ == "__main__":
    insert_prev_next_links()
