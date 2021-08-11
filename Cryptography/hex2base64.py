from base64 import b64encode

hex_string = input("Enter a hex string: ")

b64_string = b64encode(bytes.fromhex(hex_string)).decode()
print(b64_string)
