def text_encryption(data: str, key: str, alphabet: str) -> str:
    """
    Encrypt input text using a complex Caesar cipher with a key.

    :param data: Text to encrypt.
    :param key: Encryption key.
    :param alphabet: Alphabet used for encryption.
    :return: Encrypted text.
    """
    if not data or not key or not alphabet:
        raise ValueError("Data, key, and alphabet must not be empty.")

    data, key = data.lower(), key.lower()
    extended_key = (key * (len(data) // len(key) + 1))[: len(data)]
    encrypted_text = ""

    for symbol, shift in zip(data, extended_key):
        if symbol in alphabet and shift in alphabet:
            new_position = (alphabet.find(symbol) + alphabet.find(shift)) % len(
                alphabet
            )
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += symbol

    return encrypted_text


def text_decryption(encrypted_data: str, key: str, alphabet: str) -> str:
    """
    Decrypt input text encrypted with a complex Caesar cipher using a key.

    :param encrypted_data: Text to decrypt.
    :param key: Encryption key used during encryption.
    :param alphabet: Alphabet used for encryption.
    :return: Decrypted text.
    """
    if not encrypted_data or not key or not alphabet:
        raise ValueError("Encrypted data, key, and alphabet must not be empty.")

    encrypted_data, key = encrypted_data.lower(), key.lower()
    extended_key = (key * (len(encrypted_data) // len(key) + 1))[: len(encrypted_data)]
    decrypted_text = ""

    for symbol, shift in zip(encrypted_data, extended_key):
        if symbol in alphabet and shift in alphabet:
            new_position = (alphabet.find(symbol) - alphabet.find(shift)) % len(
                alphabet
            )
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += symbol

    return decrypted_text
