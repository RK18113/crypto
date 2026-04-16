import math
import struct

def left_rotate(bits, n):
    return ((bits << n) | (bits >> (32 - n))) & 0xFFFFFFFF

def F(b, c, d):
    return (b & c) | (~b & d)

def md5(msg):
    bin_msg = "".join(format(ord(char), '08b') for char in msg)
    og_msg_len = len(bin_msg)

    pad_msg = bin_msg + '1'

    while len(pad_msg) % 512 != 448:
        pad_msg += '0'

    lit_en_msg_len = struct.pack("<Q", og_msg_len)
    pad_msg += "".join(format(byte, '08b') for byte in lit_en_msg_len)

    first512 = pad_msg[:512]

    msg_words = []
    for i in range(0, 512, 32):
        block32 = first512[i:i+32]

        byte0 = block32[0:8]
        byte1 = block32[8:16]
        byte2 = block32[16:24]
        byte3 = block32[24:32]

        word = int(byte3 + byte2 + byte1 + byte0, 2)
        msg_words.append(word)

    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    sine_constants = [
        int((2**32) * abs(math.sin(i + 1))) & 0xFFFFFFFF
        for i in range(16)
    ]

    shift_constants = [7, 12, 17, 22] * 4

    print(f"A={hex(A)} B={hex(B)} C={hex(C)} D={hex(D)}")

    for step in range(16):
        F_val = F(B, C, D)
        cur_word = msg_words[step]
        cur_sine = sine_constants[step]

        temp_sum = (A + F_val + cur_word + cur_sine) & 0xFFFFFFFF
        new_B = (B + left_rotate(temp_sum, shift_constants[step])) & 0xFFFFFFFF

        A, D, C, B = D, C, B, new_B

        print(
            f"step {step+1:2d} : "
            f"A={hex(A):<10} "
            f"B={hex(B):<10} "
            f"C={hex(C):<10} "
            f"D={hex(D):<10}"
        )

    return A, B, C, D

msg = "ram12345"
A, B, C, D = md5(msg)

print("\nAfter Round 1")
print(f"A={hex(A)} B={hex(B)} C={hex(C)} D={hex(D)}")
