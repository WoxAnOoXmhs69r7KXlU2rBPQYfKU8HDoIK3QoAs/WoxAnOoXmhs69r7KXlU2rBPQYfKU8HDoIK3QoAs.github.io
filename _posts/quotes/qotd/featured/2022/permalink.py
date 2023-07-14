import os
import glob
import re

def update_permalink(folder):
    markdown_files = glob.glob(os.path.join(folder, "**/*.md"), recursive=True)

    for file_path in markdown_files:
        # Extract the relative path from _posts folder
        relative_path = os.path.relpath(file_path, '_posts')
        relative_directory = os.path.dirname(relative_path)

        # Remove leading ".." in the relative path
        relative_directory = re.sub(r'^\.\.(\/|$)', '', relative_directory)

        # Extract the last number from the file name (excluding the extension)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        last_number = re.search(r'\d+$', file_name).group(0)

        # Construct the permalink
        permalink = '/quotes/qotd/featured/2022/' + relative_directory + '/' + last_number

        # Rename the file with the new permalink structure
        new_file_path = os.path.join(os.path.dirname(file_path), permalink)
        os.rename(file_path, new_file_path)

        print(f"Updated permalink in: {file_path}")

if __name__ == "__main__":
    folder_path = ""  # Set the root folder path here
    update_permalink(folder_path)
