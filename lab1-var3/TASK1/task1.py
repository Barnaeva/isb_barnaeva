def text_encryption(data: str, key: str, alphabet: str) -> str:
    """
    Encrypts the input text using a complex Caesar cipher with a key.

    :param data: The text to be encrypted.
    :param key: The encryption key.
    :param alphabet: The alphabet used for encryption.
    :return: The encrypted text.
    """
    if not data or not key or not alphabet:
        raise ValueError("Data, key, and alphabet must not be empty.")

    data, key = data.lower(), key.lower()

    extended_key = (key * (len(data) // len(key) + 1))[:len(data)]
    encrypted_text = ""

    for symbol, shift in zip(data, extended_key):
        if symbol in alphabet and shift in alphabet:
            new_position = (alphabet.find(symbol) + alphabet.find(shift)) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += symbol

    return encrypted_text
