def vigenere_enc(string, key):
    result = ""
    key = key.lower()
    j = 0

    for char in string:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            j += 1
        else:
            result += char
    return result

def vigenere_dec(string, key):
    result = ""
    key = key.lower()
    j = 0

    for char in string:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            j += 1
        else:
            result += char
    return result

# string = "ABCD"
# key = "hello"
# enc = vigenere_enc(string, key)
# print(enc)
# print(vigenere_dec(enc, key))
