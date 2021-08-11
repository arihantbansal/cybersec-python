def xor(a, b):
  return hex(int(a, 16) ^ int(b, 16))


a = input("Enter first string to XOR: ")
b = input("Enter second string: ")

print(xor(a, b)[2:])
