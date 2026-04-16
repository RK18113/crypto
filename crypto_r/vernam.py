def vernam_enc(text, key):
    return [ord(t) ^ ord(k) for t, k in zip(text, key)]    

def vernam_dec(cipher, key):
    return "".join(chr(c ^ ord(k)) for c, k in zip(cipher, key))

# text = "oak"
# key = "son"
# print (text, [ord(t) for t in text])
# cipher = vernam_enc(text, key)
# print(cipher)
# print(vernam_dec(cipher, key))
