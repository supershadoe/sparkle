"""
Server-side code

To perform Key Exchange for authenticated message transmission.

Uses ECDH for Key Exchange.
"""

import base64
import os
import typing_extensions as typing

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

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

class ServerSideExchanger:
    def __init__(self: typing.Self) -> None:
        self._key = X25519PrivateKey.generate()

    def derive(self: typing.Self, client_key: str) -> bytes:
        """
        Parameters
        ------
        server_key: The server-side key in url-safe base64 encoding

        Returns
        -------
        A key derived from the shared key with that particular client.
        The key isn't persisted internally as a broker can have multiple
        clients.
        """
        raw_client_key = base64.urlsafe_b64decode(client_key)
        client_public_key = X25519PublicKey.from_public_bytes(raw_client_key)
        shared_key = self._key.exchange(client_public_key)
        return HKDF(
            algorithm=SHA256(),
            length=16,
            salt=None,
            info=None,
        ).derive(shared_key)

    @property
    def public_key(self: typing.Self) -> X25519PublicKey:
        return base64.urlsafe_b64encode(
            self._key.public_key().public_bytes_raw()
        )

__all__ = [ Decryptor, ServerSideExchanger ]
