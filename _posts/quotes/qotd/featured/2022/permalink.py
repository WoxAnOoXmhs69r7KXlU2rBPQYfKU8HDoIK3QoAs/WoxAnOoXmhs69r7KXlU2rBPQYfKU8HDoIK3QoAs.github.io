import os
import glob
import re

def update_markdown_files(folder):
    markdown_files = glob.glob(os.path.join(folder, "**/*.md"), recursive=True)

    for file_path in markdown_files:
        with open(file_path, 'r') as file:
            content = file.read()

        match = re.match(r'^---\n(.+?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            body = match.group(2)

            file_name = os.path.splitext(os.path.basename(file_path))[0]
            last_number = re.search(r'\d+$', file_name).group(0)

            relative_path = os.path.relpath(file_path, '_posts')
            relative_directory = os.path.dirname(relative_path)

            relative_directory = re.sub(r'^\.\.(\/|$)', '', relative_directory)

            permalink = '/quotes/qotd/featured/2022/' + relative_directory + '/' + last_number

            if 'permalink:' in frontmatter:
                frontmatter = re.sub(r'permalink:\s*(.*)', f'permalink: {permalink}', frontmatter)
            else:
                frontmatter = f'permalink: {permalink}\n' + frontmatter

            updated_content = f'---\n{frontmatter}\n---\n{body}'

            with open(file_path, 'w') as file:
                file.write(updated_content)

            print(f"Updated metadata in: {file_path}")

if __name__ == "__main__":
    folder_path = "" 
    update_markdown_files(folder_path)
