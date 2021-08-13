from tqdm import tqdm  # For progress bar
from binascii import hexlify


def encode_xor(msg, key):
  return bytes([msg[i] ^ key[i % len(key)] for i in tqdm(range(len(msg)))])


message = input("Enter your message: ").encode()
key = input("Enter key: ").encode()

ciphertext = encode_xor(message, key)
print("-" * 140)
print("Ciphertext: ", hexlify(ciphertext))
