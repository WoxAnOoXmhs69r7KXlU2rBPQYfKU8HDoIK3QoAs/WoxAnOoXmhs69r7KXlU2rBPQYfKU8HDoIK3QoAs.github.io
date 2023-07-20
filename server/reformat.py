import os
import re
import shutil

def rename_and_move_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            match = re.match(r'(\d{4}-\d{2}-\d{2})-.*-(\d+)-(\d+)\.md', filename)
            if match:
                date = match.group(1)
                second_last_number = match.group(2)
                new_folder = date[-2:]
                new_filename = f'{date}-{second_last_number}.md'

                new_folder_path = os.path.join(directory, new_folder)
                os.makedirs(new_folder_path, exist_ok=True)
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(new_folder_path, new_filename)

                shutil.move(old_file_path, new_file_path)
                print(f'Moved and renamed: {filename} -> {new_file_path}')

rename_and_move_files('.')
