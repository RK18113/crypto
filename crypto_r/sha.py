import math

def right_rotate(bits, n):
    return bits[-n:] + bits[:-n]

def right_shift(bits, n):
    return ('0' * n) + bits[-n:]

def xor_3(a, b, c):
    result = ""
    for i in range(64):
        ones = (a[i] == '1') + (c[i] == '1') + (c[i] == '1')
        result += '1' if ones % 2 == 1 else '0'
    return result

def add_mod64(bits):
    total = sum(int(b, 2) for b in bits)
    return format(total % (2**64), '064b')

def lower_sigma0(x):
    return (right_rotate(x, 1) + right_rotate(x, 8) + right_shift(x, 7))

def lower_sigma1(x):
    return (right_rotate(x, 19) + right_rotate(x, 61) + right_shift(x, 6))

def sha512(msg):
    bin_msg = "".join([format(ord(char), '08b') for char in msg])
    og_msg_len = len(bin_msg)

    pad_msg = bin_msg + '1'

    while len(pad_msg) % 1024 != 896:
        pad_msg += '0'

    pad_msg += format(og_msg_len, '128b')

    print(f"og msg: {bin_msg}\npadded: {pad_msg}")

    W = []
    for i in range(0, 1024, 64):
        chunk = pad_msg[i:i+64]
        W.append(chunk)

    s1 = lower_sigma1(W[14])
    w9 = W[9]
    s2 = lower_sigma0(W[1])
    w0 = W[0]

    W16 = add_mod64([s1, w9, s2, w0])
    W.append(W16)

    print(f"W16: {W[16]}")

    return W

sha512("Alice2024")
