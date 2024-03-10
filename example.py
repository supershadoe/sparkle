import time

from src.client import ClientSideExchanger, Encryptor
from src.server import ServerSideExchanger, Decryptor

server_exchanger = ServerSideExchanger()

# Perform key exchange using ECDH
client_exchanger = ClientSideExchanger()
client_exchanger.derive(server_exchanger.public_key)
plaintext = b'This is a secret.'
start = time.time()
nonce, ciphertext = Encryptor.encrypt(plaintext, client_exchanger.derived_key)
end = time.time()
print(
    'Client side\n'
    f'Plain text: {plaintext}\n'
    f'Cipher text: {ciphertext.hex()}\n'
    f'Time to encrypt: {end - start}'
)

derived_key = server_exchanger.derive(client_exchanger.public_key)
server_plaintext = Decryptor.decrypt(ciphertext, derived_key, nonce)
print(f'\nServer side\nDecrypted text: {server_plaintext}')
