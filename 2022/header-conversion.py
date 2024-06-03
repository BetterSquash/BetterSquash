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
        r'<link rel="stylesheet" href="/css/bettersquash.css">': '<link href="https://bettersquash.com/css/bettersquash2024.css" rel="stylesheet"/>',
        r'<style>[\s\S]*?<\/style>': '<style></style>',
        r'<header class="bg-black-90 fixed w-100 ph3 pv3 pv4-ns ph4-m ph7-l sans-serif">\s*<nav class="f6 fw6 ttu tracked">\s*<a class="link dim white dib mr3" href="/index.html">Home</a>\s*<a class="link dim white dib mr3" href="/articles.html">Articles</a>\s*<a class="link dim white dib mr3" href="https://youtube.com/bettersquash/">Videos</a>\s*<a class="link dim white dib" href="/services.html">Services</a>\s*</nav>\s*</header>': '<header>\n<nav class="topnav">\n<a href="/index.html">HOME</a> . <a href="/articles.html">ARTICLES</a> . <a href="https://youtube.com/bettersquash">VIDEOS</a><sup><svg height="12px" id="ytsvg" version="1.1" viewbox="0 0 461.001 461.001" width="12px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g><path d="M365.257,67.393H95.744C42.866,67.393,0,110.259,0,163.137v134.728c0,52.878,42.866,95.744,95.744,95.744h269.513c52.878,0,95.744-42.866,95.744-95.744V163.137C461.001,110.259,418.135,67.393,365.257,67.393zM300.506,237.056l-126.06,60.123c-3.359,1.602-7.239-0.847-7.239-4.568V168.607c0-3.774,3.982-6.22,7.348-4.514l126.06,63.881C304.363,229.873,304.298,235.248,300.506,237.056z" style="fill:#F61C0D;"></path></g></svg></sup> . <a href="/services.html">SERVICES</a>\n</nav>',
        r'<header class="bg-colour sans-serif">\s*<div class="mw9 center pa4 pt5-ns ph7-l pt7">\s*<h1 class="f2 f1-m f-headline-l measure-narrow lh-title mv0 pt3">\s*<span class="bg-white lh-copy black pa1 tracked-tight">\s*BETTERSQUASH\s*</span>\s* <br>': '<p class="phlarge">BETTERSQUASH</p>',
        r'<span class="bg-black-90 lh-copy white pa1 tracked-tight">\s*': '<div class="theader">\n<h1 class="tcolor">',
        r'\s*</span>\s*</h1>\s*<h2 class="f3 fw1 georgia i">': '</h1>\n</div>\n<h2 class="iheader">',
        r'</h2>\s*</div>\s*</header>\s*<!--Details Begin-->\s*<div class="tl bt b--black-10 bg-light-silver black" id="details">\s*<div class="pa4 ph7-l courier mw9-l center">': '</h2>',
        r'<p class="f5 mb2 dib ttu tracked reading-time">': '<p><em>',
        r'<span class="white">/</span>': '<span class="greydash">/</span>',
        r'Translate&#8599;</a>': 'Translate</a></em><sup><svg data-name="elsvg" height="12px" viewbox="0 0 100 125" width="12px" x="0px" xmlns="http://www.w3.org/2000/svg" y="0px"><path d="M87.12,10.51H56.18a2,2,0,0,0-2,2v8a2,2,0,0,0,2,2H68.64l-26,25.08a2,2,0,0,0,0,2.85l5.65,5.66a2,2,0,0,0,2.81,0L77.13,31V43a2,2,0,0,0,2,2h8a2,2,0,0,0,2-2V12.51A2,2,0,0,0,87.12,10.51Z"></path><path d="M87.13,55.51h-8a1.94,1.94,0,0,0-2,1.89V77.59H22.05V22.47H42.23a1.94,1.94,0,0,0,1.89-2v-8a1.94,1.94,0,0,0-1.89-2H12a1.8,1.8,0,0,0-1.26.52l-.06.05-.05.06a1.8,1.8,0,0,0-.52,1.26V87.66a1.84,1.84,0,0,0,.52,1.26l.05.06.06,0a1.8,1.8,0,0,0,1.26.52H87.23A1.84,1.84,0,0,0,88.5,89l0,0,.06-.06a1.83,1.83,0,0,0,.51-1.26V57.4A1.94,1.94,0,0,0,87.13,55.51Z"></path></svg></sup>',
        r'</p>\s*</div>\s*</div>\s*<!--Details End-->\s*<div class="pa4 ph7-l Avenir mw9-l center">': '</p>\n</header>\n<hr class="content"/>',
        r'<p class="f5 f3-ns lh-copy measure sans-serif">': '<p>',
        r'class="w-100"': 'class="responsive"',
        r'<a class="norm" ': '<a ',
        r'<h2 class="f2 lh-solid sans-serif">': '<h2>',
        r'<p class="f6 sans-serif mid-gray i">Original photo by <a class="norm" href="https://www.instagram.com/rpzil/">Petteri Repo</a></p>': '',
        
        # Add more pairs as needed
    }

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            replace_in_file(file_path, replacements)
            print(f"Processed {file_name}")

if __name__ == "__main__":
    main()