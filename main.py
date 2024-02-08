import binascii

def encrypt(bin_str) -> str:
    """Takes a binary string and encrypts it."""
    hex_str = str(binascii.hexlify(bin_str), encoding='utf-8')

    return hex_str

def decrypt(encrypted_str: str):
    """Takes an encrypted string and decrypts it."""
    bin_str = binascii.unhexlify(bytes(encrypted_str.encode("utf-8")))
    return bin_str

def read_file(filename: str):
    """Takes a file and reads its contents as a binary string"""
    with open(filename, mode="rb") as file:
        return file.read()

def main():
    file = "2023-11-17 11-05-49.mkv"
    new_file = "test.mkv"
    binary_str = read_file(file)
    # print(binary_str)
    encrypted_str = encrypt(binary_str)
    # print(encrypted_str)
    decrypted_str = decrypt(encrypted_str)
    # print(decrypted_str)
    with open(new_file, "wb") as nfile:
        nfile.write(decrypted_str)


if __name__ == "__main__":
    main()
