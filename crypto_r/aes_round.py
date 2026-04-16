def print_matrix(title, matrix):
    for row in matrix:
        print(" ".join(f"{x:02X}" for x in row))

def hex_to_column_major_matrix(hex_string):
    b = [int(hex_string[i:i+2], 16) for i in range(0, 32, 2)]
    m = [[0]*4 for _ in range(4)]
    for c in range(4):
        for r in range(4):
            m[r][c] = b[c*4+r]
    return m

def multiply_by_2(x):
    y = (x << 1) & 0xFF
    if x & 0x80:
        y ^= 0x1B
    return y

def multiply_by_3(x):
    return multiply_by_2(x) ^ x

def aes_single_round(state_hex, key_hex):
    state = hex_to_column_major_matrix(state_hex)
    key = hex_to_column_major_matrix(key_hex)

    print_matrix("Initial State Matrix", state)

    for r in range(4):
        for c in range(4):
            state[r][c] = SBOX[state[r][c]]

    print_matrix("After SubBytes", state)

    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]

    print_matrix("After ShiftRows", state)

    mixed = [[0]*4 for _ in range(4)]

    for c in range(4):
        c0,c1,c2,c3 = state[0][c],state[1][c],state[2][c],state[3][c]

        mixed[0][c] = multiply_by_2(c0) ^ multiply_by_3(c1) ^ c2 ^ c3
        mixed[1][c] = c0 ^ multiply_by_2(c1) ^ multiply_by_3(c2) ^ c3
        mixed[2][c] = c0 ^ c1 ^ multiply_by_2(c2) ^ multiply_by_3(c3)
        mixed[3][c] = multiply_by_3(c0) ^ c1 ^ c2 ^ multiply_by_2(c3)

    state = mixed

    print_matrix("After MixColumns", state)

    for r in range(4):
        for c in range(4):
            state[r][c] ^= key[r][c]

    print_matrix("After AddRoundKey", state)

    return state

initial_state = "00112233445566778899AABBCCDDEEFF"
round_key = "2B7E151628AED2A6ABF7158809CF4F3C"

aes_single_round(initial_state, round_key)
