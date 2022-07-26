# # Caesar Cipher

def shift(letter, shift_amount):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_index = alphabet.index(letter) # return index of letter in alphabet
    message_letter_index = (letter_index + shift_amount) % 26
    return alphabet[message_letter_index]

# def caesar_cipher(ciphertext, shift_amount):
#     message = ''
#     for letter in ciphertext:
#         message += shift(letter, shift_amount)
#     return message

# #ciphertext = 'KDSSBWXHVGDB'
# ciphertext = 'PHHWDWWKHEULGJHDWGDZQ'
# #print(caesar_cipher(ciphertext, 3))
# for shift_amount in range(1, 26):
#     print(caesar_cipher(ciphertext, shift_amount))

# Vigenere Cipher
import math

# def vigenere_encrypt(message, key):
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # duplicate the key so that it is at least as long as the message
#     key = key * math.ceil(len(message) / len(key))# key * length_of_message/length_of_key
#     # shift each letter in the message, using the key for shift amount
#     ciphertext = ''
#     for index in range(len(message)):
#         ciphertext += shift(message[index], 1 + alphabet.index(key[index]))
#     return ciphertext

# message = 'MEETATDUSK'
# print(vigenere_encrypt(message, 'ABC'))

def vigenere_decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key * math.ceil(len(ciphertext)/len(key))
    message = ''
    for index in range(len(ciphertext)):
        message += shift(ciphertext[index], -(1 + alphabet.index(key[index])))
    return message

ciphertext = 'NGHUCWEWVL'
print(vigenere_decrypt(ciphertext, 'ABC'))