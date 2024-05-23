from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
import os

def read_key():
    """
    Read the encrypted AES key and the RSA private key from files.

    Returns:
        tuple: The encrypted AES key and the RSA private key.
    """
    with open('thekey.key', 'rb') as thekey:
        encrypted_key = thekey.read()
    with open('privkey.key', 'rb') as thekey:
        privkey = RSA.import_key(thekey.read())
    return encrypted_key, privkey

def decrypt_key(encrypted_key, privkey):
    """
    Decrypt an AES key using an RSA private key.

    Args:
        encrypted_key (bytes): The encrypted AES key.
        privkey (RSA.RsaKey): The RSA private key.

    Returns:
        bytes: The decrypted AES key.
    """
    decryptor = PKCS1_OAEP.new(privkey)
    return decryptor.decrypt(encrypted_key)

def decrypt_data(files, key):
    """
    Decrypt the contents of a list of files using AES.

    Args:
        files (list): List of file paths to decrypt.
        key (bytes): The AES key for decryption.
    """
    for file in files:
        try:
            with open(file, 'rb') as thefile:
                iv = thefile.read(16)
                contents = thefile.read()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_contents = unpad(cipher.decrypt(contents), AES.block_size)
            original_file_path = os.path.splitext(file)[0]
            with open(original_file_path, "wb") as the_file:
                the_file.write(decrypted_contents)
            os.remove(file)
        except Exception:
            continue
