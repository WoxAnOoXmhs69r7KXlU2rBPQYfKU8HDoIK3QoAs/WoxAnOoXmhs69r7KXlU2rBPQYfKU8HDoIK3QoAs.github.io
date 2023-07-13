import os
import glob
import re

def update_markdown_files(folder):
    markdown_files = glob.glob(os.path.join(folder, "**/*.md"), recursive=True)

    for file_path in markdown_files:
        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the file contains YAML frontmatter
        match = re.match(r'^---\n(.+?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            body = match.group(2)

            # Check if categories metadata is present in the frontmatter
            if 'categories:' in frontmatter:
                categories = re.search(r'categories:\s*(.*)', frontmatter).group(1)
                tags = re.sub(r'([A-Za-z]+)', r'\1', categories)  # Remove square brackets from categories

                # Update categories line to tags
                frontmatter = re.sub(r'categories:\s*(.*)', f'tags: {tags}', frontmatter)
            else:
                # Add default categories line
                frontmatter += '\ncategories: [Quotes, Featured quotes, QOTD]\n'

            # Extract the last number from the file name (excluding the extension)
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            last_number = re.search(r'\d+$', file_name).group(0)

            # Extract the relative path from _posts folder (excluding the file name)
            relative_path = os.path.relpath(file_path, '_posts')
            relative_directory = os.path.dirname(relative_path)
            permalink = os.path.join(relative_directory, last_number)
            permalink = '/' + permalink.replace('\\', '/')
            permalink += '.md'

            # Check if permalink is already present in the frontmatter
            if 'permalink:' in frontmatter:
                frontmatter = re.sub(r'permalink:\s*(.*)', f'permalink: {permalink}', frontmatter)
            else:
                frontmatter = f'permalink: {permalink}\n' + frontmatter

            updated_content = f'---\n{frontmatter}---\n{body}'

            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(updated_content)

            print(f"Updated metadata in: {file_path}")

if __name__ == "__main__":
    folder_path = "_posts"  # Set the root folder path here
    update_markdown_files(folder_path)
