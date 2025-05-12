from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def serialize_private_key(private_key, filepath: str) -> None:
    """
    Serialize and save a private RSA key to a PEM file

    :param private_key: private key
    :param filepath: file path
    :raises Exception: On failure to write the file
    """
    try:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(filepath, 'wb') as f:
            f.write(pem)
    except Exception as exc:
        raise Exception(f"Error serializing private key: {exc}")


def serialize_public_key(public_key, filepath: str) -> None:
    """
    Serialize and save a public RSA key to a PEM file

    :param public_key: public key
    :param filepath: file path
    :raises Exception: On failure to write the file
    """
    try:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(filepath, 'wb') as f:
            f.write(pem)
    except Exception as exc:
        raise Exception(f"Error serializing public key: {exc}")


def deserialize_private_key(filepath: str):
    """
    Load and deserialize a private RSA key from a PEM file

    :param filepath: file path
    :return: deserialized private key
    :raises Exception: On failure to read or parse the key
    """
    try:
        with open(filepath, 'rb') as f:
            key_bytes = f.read()
        return load_pem_private_key(key_bytes, password=None)
    except Exception as exc:
        raise Exception(f"Error deserializing private key: {exc}")


def deserialize_public_key(filepath: str):
    """
    Load and deserialize a public RSA key from a PEM file

    :param filepath: file path
    :return: deserialized public key
    :raises Exception: On failure to read or parse the key
    """
    try:
        with open(filepath, 'rb') as f:
            key_bytes = f.read()
        return load_pem_public_key(key_bytes)
    except Exception as exc:
        raise Exception(f"Error deserializing public key: {exc}")


def serialize_symmetric_key(key: bytes, filepath: str) -> None:
    """
    Save a symmetric key to a file

    :param key: symmetric key
    :param filepath: file path
    :raises Exception: On failure to write the file
    """
    try:
        with open(filepath, 'wb') as f:
            f.write(key)
    except Exception as exc:
        raise Exception(f"Error serializing symmetric key: {exc}")


def deserialize_symmetric_key(filepath: str) -> bytes:
    """
    Load a symmetric key from a file

    :param filepath: file path
    :return: symmetric key
    :raises Exception: On failure to read the file
    """
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except Exception as exc:
        raise Exception(f"Error deserializing symmetric key: {exc}")
