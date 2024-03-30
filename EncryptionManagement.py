# This file contains operations for encrypting and decrypting binary strings
from encryption import encrypt, decrypt
import binascii
import os
import random

def encrypt_file(file_path, key):
    """Reads a file and encrypts it into a string. Returns the encrypted file and encryption key."""
    with open(file_path, mode="rb") as file:
        bin_str = file.read()

    hex_str = str(binascii.hexlify(bin_str), encoding='utf-8')

    # Fancy encryption stuff here
    # Make it so that the file name is also encrypted and stored in the file for later retrieval

    hex_str = encrypt(hex_str, key)

    return hex_str, key

def decrypt_file(file_path, key):
    """Reads a file and decrypts it into a binary string object. Returns the binary string and original file name"""
    with open(file_path, mode="r") as file:
        hex_string = file.read()

    # Fancy decryption stuff here'
    hex_string = decrypt(hex_string, key)
    # Have it retrieve the file name somehow
    name = "Test_file.txt"

    bin_string = binascii.unhexlify(bytes(hex_string.encode("utf-8")))
    return bin_string, name

def make_private_key():
    if not os.path.exists("private_key.txt"):
        with open("private_key.txt", "w") as f:
            f.write(str(random.randint(1,10000000)))
            f.close()
