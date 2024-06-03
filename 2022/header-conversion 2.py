import os
import re

def replace_in_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for find_text, replace_text in replacements.items():
        content = re.sub(find_text, replace_text, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Define your find and replace pairs here
    replacements = {
        r'</header>\s*<!--Details Begin-->\s*<div class="tl bt b--black-10 bg-light-silver black" id="details">\s*<div class="pa4 ph7-l courier mw9-l center">': '',
         
        # r'Translate&#8599;</a>': 'Translate</a></em><sup><svg data-name="elsvg" height="12px" viewbox="0 0 100 125" width="12px" x="0px" xmlns="http://www.w3.org/2000/svg" y="0px"><path d="M87.12,10.51H56.18a2,2,0,0,0-2,2v8a2,2,0,0,0,2,2H68.64l-26,25.08a2,2,0,0,0,0,2.85l5.65,5.66a2,2,0,0,0,2.81,0L77.13,31V43a2,2,0,0,0,2,2h8a2,2,0,0,0,2-2V12.51A2,2,0,0,0,87.12,10.51Z"></path><path d="M87.13,55.51h-8a1.94,1.94,0,0,0-2,1.89V77.59H22.05V22.47H42.23a1.94,1.94,0,0,0,1.89-2v-8a1.94,1.94,0,0,0-1.89-2H12a1.8,1.8,0,0,0-1.26.52l-.06.05-.05.06a1.8,1.8,0,0,0-.52,1.26V87.66a1.84,1.84,0,0,0,.52,1.26l.05.06.06,0a1.8,1.8,0,0,0,1.26.52H87.23A1.84,1.84,0,0,0,88.5,89l0,0,.06-.06a1.83,1.83,0,0,0,.51-1.26V57.4A1.94,1.94,0,0,0,87.13,55.51Z"></path></svg></sup>',
       # r'</header>\s*</div>\s*</div>\s*<!--Details End-->\s*<div class="pa4 ph7-l Avenir mw9-l center">': '</p>\n</header>\n<hr class="content"/>',
      #  r'<p class="f5 f3-ns lh-copy measure sans-serif">': '<p>',
      # r'class="w-100"': 'class="responsive"',
      #  r'<a class="norm" ': '<a ',
      #  r'<h2 class="f2 lh-solid sans-serif">': '<h2>',
       # r'<p class="f6 sans-serif mid-gray i">Original photo by <a class="norm" href="https://www.instagram.com/rpzil/">Petteri Repo</a></p>': '',
        
        # Add more pairs as needed
    }

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            replace_in_file(file_path, replacements)
            print(f"Processed {file_name}")

if __name__ == "__main__":
    main()