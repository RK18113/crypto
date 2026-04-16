P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
P8 = [5, 2, 6, 3, 7, 4, 9, 8]
P4 = [1, 3, 2, 0]
IP = [1, 5, 2, 0, 3, 7, 4, 6]
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]
EP = [3, 0, 1, 2, 1, 2, 3, 0]

SBOX0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

SBOX1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(bits, table):
    return "".join(bits[i] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join('0' if i == j else '1' for i, j in zip(a, b))

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], "02b")

def F(right, key):
    expand = permute(right, EP)
    xored = xor(expand, key)
    left4, right4 = xored[:4], xored[4:]
    s0 = sbox_lookup(left4, SBOX0)
    s1 = sbox_lookup(right4, SBOX1)
    return permute(s0 + s1, P4)

def genkey(key):
    p10_key = permute(key, P10)
    left, right = p10_key[:5], p10_key[5:]

    l1 = left_shift(left, 1)
    r1 = left_shift(right, 1)
    k1 = permute(l1 + r1, P8)

    l2 = left_shift(l1, 2)
    r2 = left_shift(r1, 2)
    k2 = permute(l2 + r2, P8)

    return k1, k2

def sdes(msg, key):
    k1, k2 = genkey(key)

    init_per = permute(msg, IP)

    left, right = init_per[:4], init_per[4:]
    f_res = F(right, k1)
    left = xor(left, f_res)
    left, right = right, left

    f_res = F(right, k2)
    left = xor(left, f_res)

    combined = left + right
    return permute(combined, IP_INV)

def sdes_dec(msg, key):
    k1, k2 = genkey(key)
    k1, k2 = k2, k1

    init_per = permute(msg, IP)

    left, right = init_per[:4], init_per[4:]
    f_res = F(right, k1)
    left = xor(left, f_res)
    left, right = right, left

    f_res = F(right, k2)
    left = xor(left, f_res)

    combined = left + right
    return permute(combined, IP_INV)

plaintext = "10101010"
master_key = "1010000010"

cipher = sdes(plaintext, master_key)
decrypted = sdes_dec(cipher, master_key)

print(f"cipher: {cipher}")
print(f"plaintext: {decrypted}")
