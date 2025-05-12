from AsymmetricAlg import AsymmetricAlg
from SymmetricAlg import SymmetricAlg
from Serialization import (
    serialize_public_key, serialize_private_key,
    serialize_symmetric_key, deserialize_private_key,
    deserialize_symmetric_key
)
from io_operations import read_byte, write_byte, write_file


def generate_keys(encrypted_key_path: str, public_key_path: str, private_key_path: str) -> None:
    """
    Generate and save hybrid encryption keys.

    Args:
        encrypted_key_path: encrypted symmetric key
        public_key_path: public RSA key
        private_key_path: private RSA key
    """
    symmetric_key = SymmetricAlg().generate_key()

    private_key, public_key = AsymmetricAlg().generate_keys()

    serialize_public_key(public_key, public_key_path)
    serialize_private_key(private_key, private_key_path)
    serialize_symmetric_key(
        AsymmetricAlg(public_key=public_key).encrypt_key(symmetric_key),
        encrypted_key_path
    )


def encrypt_file(input_file: str, private_key_path: str, encrypted_key_path: str, output_file: str) -> None:
    """
    Encrypt file using hybrid encryption system

    Args:
        input_file: Path to plaintext file
        private_key_path: Path to private RSA key
        encrypted_key_path: Path to encrypted symmetric key
        output_file: Path for encrypted output
    """
    private_key = deserialize_private_key(private_key_path)
    symmetric_key = AsymmetricAlg(private_key=private_key).decrypt_key(
        deserialize_symmetric_key(encrypted_key_path)
    )

    plaintext = read_byte(input_file)
    nonce, ciphertext = SymmetricAlg(symmetric_key).encrypt(plaintext.decode('utf-8'))

    write_byte(output_file, nonce + ciphertext)


def decrypt_file(input_file: str, private_key_path: str, encrypted_key_path: str, output_file: str) -> None:
    """
    Decrypt file using hybrid encryption system.

    Args:
        input_file: Path to encrypted file
        private_key_path: Path to private RSA key
        encrypted_key_path: Path to encrypted symmetric key
        output_file: Path for decrypted output
    """
    private_key = deserialize_private_key(private_key_path)
    symmetric_key = AsymmetricAlg(private_key=private_key).decrypt_key(
        deserialize_symmetric_key(encrypted_key_path)
    )

    encrypted_data = read_byte(input_file)
    nonce, ciphertext = encrypted_data[:16], encrypted_data[16:]

    plaintext = SymmetricAlg(symmetric_key).decrypt(ciphertext, nonce)
    write_file(output_file, plaintext)