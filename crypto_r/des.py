def hex_to_bin(x, bits=64):
    return bin(int(x, 16))[2:].zfill(bits)

def bin_to_hex(x):
    return hex(int(x, 2))[2:].upper().zfill(len(x)//4)

def permute(bits, table):
    return "".join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join("0" if i == j else "1" for i, j in zip(a, b))

def s_box_substitution(bits48):
    out = ""
    for i in range(8):
        chunk = bits48[i*6:(i+1)*6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        val = S_BOXES[i][row][col]
        out += format(val, "04b")
    return out

def des_algorithm(pt_hex, key_hex):
    key = hex_to_bin(key_hex, 64)
    key56 = permute(key, PC1)
    C, D = key56[:28], key56[28:]

    subkeys = []

    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkeys.append(permute(C + D, PC2))

    pt = hex_to_bin(pt_hex, 64)
    ip = permute(pt, IP)
    L, R = ip[:32], ip[32:]

    print("--- Task 1: Perform Initial Permutation ---")
    print("L0:", bin_to_hex(L), "| R0:", bin_to_hex(R), "\n")

    print("--- Task 2: Execute 16 Rounds ---")

    for rnd in range(16):
        old_R = R
        expanded = permute(R, E_BOX)
        x = xor(expanded, subkeys[rnd])
        subbed = s_box_substitution(x)
        f = permute(subbed, P_BOX)
        R = xor(L, f)
        L = old_R
        print(f"Round {rnd+1:2d} -> L: {bin_to_hex(L)} | R: {bin_to_hex(R)}")

    print("\n--- Task 3: Apply Final Permutation ---")

    pre_output = R + L
    cipher_bin = permute(pre_output, FP)
    cipher_hex = bin_to_hex(cipher_bin)

    print("Pre-FP State (Swapped R+L):", bin_to_hex(pre_output))
    print("Final Ciphertext (Hex):    ", cipher_hex)

    return cipher_hex

pt = "0123456789ABCDEF"
key = "133457799BBCDFF1"

des_algorithm(pt, key)
