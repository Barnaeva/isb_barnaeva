import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


class SymmetricAlg:
    def __init__(self, key=None):
        """
        Initialize symmetric encryption handler

        :param key: Optional existing key (32 bytes for ChaCha20)
        """
        self.__key = key
        self.__nonce = os.urandom(16)

    def generate_key(self) -> bytes:
        """
        Generate new random symmetric key

        :return: 32-byte key
        """
        self.__key = os.urandom(32)
        return self.__key

    def encrypt(self, plaintext: str) -> tuple[bytes, bytes]:
        """
        Encrypt text with ChaCha20

        :param plaintext: Text to encrypt
        :return: Tuple of (nonce, ciphertext)
        """
        # 1. Prepare data with padding
        padder = padding.ANSIX923(32).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        # 2. Encrypt
        cipher = Cipher(algorithms.ChaCha20(self.__key, self.__nonce), mode=None)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return self.__nonce, ciphertext

    def decrypt(self, ciphertext: bytes, nonce: bytes) -> str:
        """
        Decrypt ChaCha20 message

        :param ciphertext: Encrypted data
        :param nonce: Nonce used for encryption
        :return: Decrypted string
        """
        cipher = Cipher(algorithms.ChaCha20(self.__key, nonce), mode=None)
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.ANSIX923(32).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data.decode()
