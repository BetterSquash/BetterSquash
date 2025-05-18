import os

# CONFIGURATION
domain = 'https://squashquestions.com/'
questions_folder = 'questions'
extra_files = ['random.html']
exclude_files = ['404.html', 'privacy.html']
output_file = 'sitemap.xml'

# Helper to create <url> entries
def url_entry(loc):
    return f'  <url>\n    <loc>{loc}</loc>\n  </url>'

# Gather question URLs
question_urls = []
for filename in os.listdir(questions_folder):
    if filename.endswith('.html'):
        full_url = f"{domain}{questions_folder}/{filename}"
        question_urls.append(url_entry(full_url))

# Include selected root-level pages
for filename in extra_files:
    if filename not in exclude_files and os.path.exists(filename):
        full_url = f"{domain}{filename}"
        question_urls.append(url_entry(full_url))

# Create sitemap content
sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(question_urls)}
</urlset>
'''

# Write to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f'✅ {output_file} created with {len(question_urls)} URLs.')
