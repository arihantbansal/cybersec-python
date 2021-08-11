from pprint import pprint


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
  # with the exception of ' ', which I found on an archived webpage.
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


def single_byte_attack(ciphertext):
  potential_msgs = []
  for possible_key in range(256):
    msg = bxor(ciphertext, possible_key)
    score = get_english_score(msg)
    msg_data = {
        "message": msg,
        "score": score,
        "key": possible_key
    }
    potential_msgs.append(msg_data)

  best_score = sorted(
      potential_msgs, key=lambda x: x["score"], reverse=True)
  # print(best_score)
  # for item in best_score:
  #   print("{}: {}".format(item.title(), best_score[item]))
  return best_score[0]


ciphertext = bytes.fromhex(input("Enter hex encoded string: "))

# Dirty implementation to check for the answer
# for i in range(256):
#   print(bxor(ciphertext, i), i)

ans = single_byte_attack(ciphertext)

print("\n".join(f"{k.title()}\t{v}" for k, v in ans.items()))
