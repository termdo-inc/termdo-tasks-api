import os
import shutil

# Remove out folder
shutil.rmtree("out", ignore_errors=True)

# Remove .pytest_cache folder
shutil.rmtree(".pytest_cache", ignore_errors=True)

# Remove __pycache__ folders inside source folder
for root, folders, files in os.walk("source"):
    for folder_name in folders:
        if folder_name == "__pycache__":
            shutil.rmtree(os.path.join(root, folder_name), ignore_errors=True)
