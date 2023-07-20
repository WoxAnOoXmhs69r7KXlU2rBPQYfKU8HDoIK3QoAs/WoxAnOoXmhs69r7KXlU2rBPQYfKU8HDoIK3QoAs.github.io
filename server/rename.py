import os
import re

pattern = r'^(\d{4}-\d{2}-\d{2})-(\d+)\.md$'
replacement = r'\1-qotdf-\1\2.md'

directory = '.'  
md_files = [filename for filename in os.listdir(directory) if filename.endswith('.md')]

for filename in md_files:
    new_filename = re.sub(pattern, replacement, filename)
    if new_filename != filename:
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed {filename} to {new_filename}')
