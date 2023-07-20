import os
import yaml

def add_permalink_link(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    frontmatter_end = lines.index('---\n', 1) 

    frontmatter = yaml.safe_load(''.join(lines[1:frontmatter_end])) 

    permalink = frontmatter.get('permalink')
    if permalink:
        link = f"link: https://quotes.yeahgames.net{permalink}\n"
        lines.insert(frontmatter_end, link) 

        with open(file_path, 'w') as file:
            file.writelines(lines) 

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        file_path = os.path.join(directory, filename)
        add_permalink_link(file_path)
