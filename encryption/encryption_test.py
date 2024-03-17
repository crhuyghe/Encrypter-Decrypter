from elliptic_curve import generatePublicKey, generateSharedSecret
from secrets import randbits
from aes_encrypt import encrypt, decrypt

private_key_alice = randbits(256)
public_key_alice = generatePublicKey(private_key_alice)

private_key_bob = randbits(256)
public_key_bob = generatePublicKey(private_key_bob)

# Key exchange using ECDH
shared_secret_alice = generateSharedSecret(private_key_alice, public_key_bob)[0]
shared_secret_bob = generateSharedSecret(private_key_bob, public_key_alice)[0]

if shared_secret_alice == shared_secret_bob:
    print("Shared secret successfully generated")

key = hex(shared_secret_alice)[2:].zfill(32)

data_original = key
print("original: ", data_original)
data_encrypted = encrypt(data_original, key)
print("encrypted:", data_encrypted)
data_decrypted = decrypt(data_encrypted, key)
print("decrypted:", data_decrypted)

if data_original == data_decrypted:
    print("Successfully decrypted")