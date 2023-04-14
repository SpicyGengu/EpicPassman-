import binascii
import hashlib


def encrypt(master_key: str, plaintext: str) -> str:
    """Encrypts plaintext using a master key."""
    key = hashlib.sha256(master_key.encode()).digest()
    plaintext_bytes = plaintext.encode()
    ciphertext_bytes = bytearray()
    for i in range(len(plaintext_bytes)):
        byte = plaintext_bytes[i] ^ key[i % len(key)]
        ciphertext_bytes.append(byte)
    ciphertexthex = binascii.hexlify(bytearray(ciphertext_bytes))
    return str(ciphertexthex, 'utf-8')


def decrypt(master_key: str, ciphertext: str) -> str:
    """Decrypts ciphertext using a master key."""
    try:
        key = hashlib.sha256(master_key.encode()).digest()
        ciphertext_bytes = bytearray.fromhex(ciphertext)
        plaintext_bytes = bytearray()
        for i in range(len(ciphertext_bytes)):
            byte = ciphertext_bytes[i] ^ key[i % len(key)]
            plaintext_bytes.append(byte)
        plaintext = plaintext_bytes.decode()
    except:
        plaintext = False
    return plaintext
