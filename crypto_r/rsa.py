import math

p = 11
q = 13

n = p*q
phi = (p-1)*(q-1)

def char2int(char):
    if char == ' ':
        return 27
    else:
         return ord(char) - 96

def int2char(num):
    if num == 27:
        return ' '
    else:
        return chr(num + 96)

e = 0
for i in range(2, phi):
    if (math.gcd(i, phi) == 1):
        e = i
        break

d = pow(e, -1, phi)

msg = "model exam"
cipher = []
# enc
for char in msg:
    num = char2int(char)
    temp = pow(num, e, n)
    cipher.append(temp)

print(cipher)
plaintext = ""
for num in cipher:
    temp = pow(num, d, n)
    char = int2char(temp)
    plaintext += char

print(plaintext)
