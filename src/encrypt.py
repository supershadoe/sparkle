"""
Encryption/Decryption code.

Uses AES-128 and LSB steganography to hide the code
"""

import os
try:
    from typing import Self
except Exception:
    from typing_extensions import Self

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CTR
from stegano import lsb

class Encryptor:
    def __init__(self: Self, image_path: str) -> None:
        self.image_path = image_path

    def encrypt(self: Self, data: bytes, key: bytes) -> tuple[bytes, bytes]:
        """
        Uses a 128 bit key and a 128 bit nonce to initialize the AES algo
        """
        nonce = os.urandom(16)
        cipher = Cipher(
            AES128(key),
            CTR(nonce),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = nonce, encryptor.update(data) + encryptor.finalize()
        return lsb.hide(self.image_path, ciphertext)

class Decryptor:
    def decrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
        ciphertext = lsb.reveal(data)
        cipher = Cipher(
            AES128(key),
            CTR(nonce),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()

__all__ = [ Encryptor, Decryptor ]
