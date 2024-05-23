from pathlib import Path
import os

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

def get_encrypted_files(path):
    """
    Get a list of encrypted files in a directory.

    Args:
        path (Path): The directory to search for files.

    Returns:
        list: List of encrypted file paths.
    """
    files = []
    for root, _, filenames in os.walk(path):
        for file_name in filenames:
            if file_name.endswith('.enc'):
                file_path = os.path.join(root, file_name)
                files.append(file_path)
    return files
