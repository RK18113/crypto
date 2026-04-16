def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    return [SBOX[b] for b in word]

def xor_words(a, b):
    return [x ^ y for x, y in zip(a, b)]

def word_to_hex(word):
    return "".join(f"{b:02X}" for b in word)

def aes_128_key_expansion(hex_key):
    key_bytes = [int(hex_key[i:i+2], 16) for i in range(0, len(hex_key), 2)]
    W = []

    for i in range(4):
        W.append(key_bytes[i*4:(i+1)*4])

    for i in range(4, 44):
        temp = W[i - 1]

        if i % 4 == 0:
            round_num = i // 4
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp = xor_words(temp, [RCON[round_num], 0, 0, 0])

        W.append(xor_words(W[i - 4], temp))

    print("Generated Round Keys:")

    for r in range(11):
        key = ""
        for j in range(4):
            key += word_to_hex(W[r*4 + j])

        if r == 0:
            print(f"Round {r:2} Key: {key} (Original Key)")
        else:
            print(f"Round {r:2} Key: {key}")

master_key = "2B7E151628AED2A6ABF7158809CF4F3C"
aes_128_key_expansion(master_key)
