def ceaser_enc(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def ceaser_dec(string, shift):
    return ceaser_enc(string, -shift)

# string = "ABCD"
# shift = 1
# enc = ceaser_enc(string, shift)
# print(enc)
# print(ceaser_dec(enc, shift))
