alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
   pass # do stuff and return ciphertext
   word = ""
   for letter in plaintext:
       position= alphabet.index(letter)
       replace=alphabet[position+k:position+k+1]
       word=word+replace
   return word 
encrypt('abcd',3)
