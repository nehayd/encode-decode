alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  encoded_string = ""
  for letter in text:
    cipher_text = alphabet[alphabet.index(letter)+shift]
    encoded_string += cipher_text
  print("The encoded text is {}".format(encoded_string))

def decrypt(text,shift):
  encoded_string = ""
  for letter in text:
    cipher_text = alphabet[alphabet.index(letter)-shift]
    encoded_string += cipher_text
  print("The encoded text is {}".format(encoded_string))

def caesar(direction):
  if direction == "encode":
    encrypt(text=text, shift=shift)
  elif direction == "decode":
    decrypt(text=text, shift=shift)

caesar(direction)