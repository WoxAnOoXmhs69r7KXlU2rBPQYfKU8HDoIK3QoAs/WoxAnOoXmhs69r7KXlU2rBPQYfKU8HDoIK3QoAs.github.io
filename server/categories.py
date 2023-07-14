import os

def add_yaml_frontmatter(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(content.replace('---', '---\ncategories: [Quotes, Featured quotes, QOTD]', 1))

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_yaml_frontmatter(file_path)
                print(f'Updated: {file_path}')

# Set the directory to scan
directory_to_scan = '.'

scan_directory(directory_to_scan)
