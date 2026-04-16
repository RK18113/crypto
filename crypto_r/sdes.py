def permute(bits, table):
    return [bits[i] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join(['0' if (i == j) else '1' for i, j in zip(a, b)])

def sbox_lookup(bits, SBOX):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)

    return format(SBOX[row][col], '02b')

def F(right, key):
    expand = permute(right, EP)

    xored = xor(expand, key)
    left4, right4 = xored[:4], xored[4:]

    s0, s1 = sbox_lookup(left4, SBOX0), sbox_lookup(right4, SBOX1)

    return permute(s0+s1, P4)

def genkey(key):
    p10_key = permute(key, P10)
    left, right = p10_key[:5], p10_key[5:]

    lsl1, lsr1 = left_shift(left, 1), left_shift(right, 1)
    key1 = permute(lsl1+lsr1, P8)

    lsl2, lsr2 = left_shift(lsl1, 2), left_shift(lsr1, 2)
    key2 = permute(lsl2+lsr2, P8)

    return key1, key2

def sdes(msg, key):
    k1, k2 = genkey(key)

    init_per = permute(msg, IP)

    # round 1
    left, right = init_per[:4], init_per[4:]
    f_res = F(right, k1)
    new_left = xor(left, f_res)
    left, right = right, new_left

    # round 2
    f_res = F(right, k2)
    new_left = xor(left, f_res)
    combined = new_left+right

    cipher = permute(combined, IP_INV)
    return cipher

def sdes_dec(msg, key):
    k2, k1 = genkey(key)

    init_per = permute(msg, IP)

    # round 1
    left, right = init_per[:4], init_per[4:]
    f_res = F(right, k1)
    new_left = xor(left, f_res)
    left, right = right, new_left

    # round 2
    f_res = F(right, k2)
    new_left = xor(left, f_res)
    combined = new_left+right

    plaintext = permute(combined, IP_INV)
    return plaintext

plaintext = "10101010"
master_key = "1010000010"

cipher = sdes(plaintext, master_key)
plaintext = sdes_dec(cipher, master_key)

print(f"cipher: {cipher}\n\nplaintext: {plaintext}")
