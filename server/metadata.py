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

            # Replace "categories" with "tags" in the frontmatter
            updated_frontmatter = frontmatter.replace("categories:", "tags:")

            # Check if "tags" line is already present in the frontmatter
            if 'tags:' not in updated_frontmatter:
                # Add default tags line
                updated_frontmatter += '\ntags: [Quotes, Featured quotes, QOTD]'

            updated_content = f'---\n{updated_frontmatter}\n---\n{body}'

            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(updated_content)

            print(f"Updated metadata in: {file_path}")

if __name__ == "__main__":
    folder_path = ""  # Set the root folder path here
    update_markdown_files(folder_path)
