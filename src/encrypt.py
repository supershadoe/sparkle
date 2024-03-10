import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CTR

class Encryptor:
    @staticmethod
    def encrypt(data: bytes, key: bytes) -> tuple[bytes, bytes]:
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
        return nonce, encryptor.update(data) + encryptor.finalize()

class Decryptor:
    @staticmethod
    def decrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
        cipher = Cipher(
            AES128(key),
            CTR(nonce),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()

__all__ = [ Encryptor, Decryptor ]
