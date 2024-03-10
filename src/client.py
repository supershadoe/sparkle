"""
Client-side code

To be integrated on the IoT nodes
"""

import base64
import os
import typing

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

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

class KeyNotDerivedError(Exception):
    pass

class ClientSideExchanger:
    def __init__(self: typing.Self) -> None:
        self._key = X25519PrivateKey.generate()
        self._derived_key = None

    def derive(self: typing.Self, server_key: str) -> bytes:
        """
        Params
        ------
        server_key: The server-side key in url-safe base64 encoding

        Returns
        -------
        A key derived from the shared key with the server.
        It is persisted and can be accessed using `derived_key` property.
        """
        raw_server_key = base64.urlsafe_b64decode(server_key)
        server_public_key = X25519PublicKey.from_public_bytes(raw_server_key)
        shared_key = self._key.exchange(server_public_key)
        self._derived_key = HKDF(
            algorithm=SHA256(),
            length=16,
            salt=None,
            info=None,
        ).derive(shared_key)
        return self._derived_key

    @property
    def derived_key(self: typing.Self) -> bytes:
        if self._derived_key is None:
            raise KeyNotDerivedError('Derive the key first using derive()')
        return self._derived_key

    @property
    def public_key(self: typing.Self) -> bytes:
        return base64.urlsafe_b64encode(
            self._key.public_key().public_bytes_raw()
        )

__all__ = [ ClientSideExchanger, Encryptor ]
