def encrypt(plaintext, k):
    return ''.join([chr(ord(i)^ord(j)) for i, j in zip(plaintext, k)])
