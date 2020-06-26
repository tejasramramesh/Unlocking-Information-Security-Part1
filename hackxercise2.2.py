alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    word=""
    for k in range(0,27):# for trying out all possibilities
        print("Key : "+ str(k))#K is the brute force key
        for c in ciphertext:
            position = alphabet.index(c)
            replace=alphabet[position-k:position-k+1]
            word=word+replace 
        
        print(word)
        word=""
    
    
    


    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
