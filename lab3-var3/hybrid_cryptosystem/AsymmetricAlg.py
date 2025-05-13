from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class AsymmetricAlg:

    @staticmethod
    def generate_keys() -> tuple:
        """
        Generate new RSA key pair.

        :return: private_key, public_key
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPrivateKey) -> bytes:
        """
        Encrypt text with public key.

        :param symmetric_key: text to encrypt
        :return: encrypted key
        """
        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return encrypted_key

    @staticmethod
    def decrypt_key(encrypted_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Decrypt data with private key.

        :param encrypted_key: encrypted bytes
        :return: decrypted key
        """
        decrypted_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return decrypted_key
