def caeser_cipher_encode(text_to_encode: str, key: int) -> str:
    """
    Encodes the given text using a Caeser cipher with the provided key.

    :param text_to_encode: The text to encode.
    :param key: The key to use for encoding.
    :return: The encoded text.
    """
    encoded_text = ""
    for char in text_to_encode:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + key) % 26 + 97)
            encoded_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            encoded_text += char
    return encoded_text