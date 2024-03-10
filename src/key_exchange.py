"""
To perform Key Exchange for authenticated message transmission.

Uses ECDH for Key Exchange.
"""

import base64
try:
    from typing import Self
except Exception:
    from typing_extensions import Self

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

class KeyExchanger:
    def __init__(self: Self) -> None:
        self._key = X25519PrivateKey.generate()

    def derive(self: Self, client_key: str) -> bytes:
        """
        Parameters
        ------
        server_key: The server-side key in url-safe base64 encoding

        Returns
        -------
        A key derived from the shared key with that particular user.
        The key isn't persisted internally.
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
    def public_key(self: Self) -> X25519PublicKey:
        return base64.urlsafe_b64encode(
            self._key.public_key().public_bytes_raw()
        )

__all__ = [ KeyExchanger ]
