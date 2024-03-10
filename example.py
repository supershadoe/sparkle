import time

from src.encrypt import Encryptor, Decryptor
from src.key_exchange import KeyExchanger

server_exchanger = KeyExchanger()

# Perform key exchange using ECDH
client_exchanger = KeyExchanger()
client_derived_key = client_exchanger.derive(server_exchanger.public_key)
plaintext = b'This is a secret.'
start = time.time()
nonce, ciphertext = Encryptor.encrypt(plaintext, client_derived_key)
end = time.time()
print(
    'Client side\n'
    f'Plain text: {plaintext}\n'
    f'Cipher text: {ciphertext.hex()}\n'
    f'Time to encrypt: {end - start}'
)

server_derived_key = server_exchanger.derive(client_exchanger.public_key)
server_plaintext = Decryptor.decrypt(ciphertext, server_derived_key, nonce)
print(f'\nServer side\nDecrypted text: {server_plaintext}')
