import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


class SymmetricAlg:
    @staticmethod
    def gen_nonce():
        return os.urandom(16)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate new random symmetric key

        :return: 32-byte key
        """
        key = os.urandom(32)
        return key

    @staticmethod
    def encrypt(plaintext: str, key: bytes, nonce: bytes) -> bytes:
        """
        Encrypt text with ChaCha20

        :param plaintext: Text to encrypt
        :param key: key
        :param nonce: nonce
        :return: Tuple of (nonce, ciphertext)
        """
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return ciphertext

    @staticmethod
    def decrypt(ciphertext: bytes, key: bytes, nonce: bytes) -> str:
        """
        Decrypt ChaCha20 message

        :param ciphertext: Encrypted data
        :param nonce: Nonce used for encryption
        :param key: key
        :return: Decrypted string
        """
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data.decode()
