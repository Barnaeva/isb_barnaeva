from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class AsymmetricAlg:

    def __init__(self, private_key=None, public_key=None):
        """
        Initialize encryption handler.

        :param private_key: private key
        :param public_key: public key
        """
        self.__private_key = private_key
        self.__public_key = public_key

    def generate_keys(self) -> tuple:
        """
        Generate new RSA key pair.

        :return: private_key, public_key
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.__private_key = keys
        self.__public_key = keys.public_key()
        return self.__private_key, self.__public_key

    def encrypt_key(self, symmetric_key: bytes) -> bytes:
        """
        Encrypt text with public key.

        :param symmetric_key: text to encrypt
        :return: encrypted key
        """
        encrypted_key = self.__public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_key

    def decrypt_key(self, encrypted_key: bytes) -> bytes:
        """
        Decrypt data with private key.

        :param encrypted_key: encrypted bytes
        :return: decrypted key
        """
        decrypted_key = self.__private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_key