import os
import shutil

def copy_markdown_files(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, file)

                shutil.copy2(source_path, destination_path)

source_directory = "." 
destination_directory = "./copied" 

copy_markdown_files(source_directory, destination_directory)
