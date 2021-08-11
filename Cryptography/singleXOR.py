from binascii import unhexlify


def bxor(input, value):
  """Returns the result of each byte being XOR'd with a single value"""
  output_bytes = b''
  for byte in input:
    output_bytes += bytes([byte ^ value])
  return output_bytes


def get_english_score(input_bytes):
  """Compares each input byte to a character frequency 
  chart and returns the score of a message based on the
  relative frequency the characters occur in the English
  language
  """

  # From https://en.wikipedia.org/wiki/Letter_frequency
  # with the exception of ' ', which has been estimated.
  character_frequencies = {
      'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
      'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
      'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
      'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
      'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
      'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
      'y': .01974, 'z': .00074, ' ': .13000
  }

  return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


ciphertext = unhexlify(input("Enter hex encoded string: "))

for i in range(256):
  print(bxor(ciphertext, i), i)
