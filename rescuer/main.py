from decryption import read_key, decrypt_key, decrypt_data
from file_operations import get_documents_path, get_encrypted_files
from system_operations import restore_wallpaper

def main():
    """
    Main function to execute the ransomware rescue operation.
    """
    encrypted_key, privkey = read_key()
    key = decrypt_key(encrypted_key, privkey)
    
    document_path = get_documents_path()
    files = get_encrypted_files(document_path)
    
    decrypt_data(files, key)
    
    original_wallpaper_path = 'path/to/original/wallpaper.png'
    restore_wallpaper(original_wallpaper_path)

if __name__ == '__main__':
    main()
