def padding(msg):
    data = bytearray(msg, 'utf-8')
    l = len(data) * 8
    
    data.append(0x80)
    
    while (len(data)*8) % 512 != 448:
        data.append(0)
    
    data += l.to_bytes(8, 'little')
    return data


def getblocks(d):
    blocks = []
    for i in range(0, len(d), 64):
        blocks.append(d[i:i+64])
    return blocks


def getword(d):
    words = []
    for i in range(0, 64, 4):
        w = (d[i]) | (d[i+1] << 8) | (d[i+2] << 16) | (d[i+3] << 24)
        words.append(w)
    return words


def md5_round(a, b, c, d, m0):
    f = (b & c) | (~b & d)
    k = 0xd76aa478
    
    temp = (a + f + k + m0) & 0xFFFFFFFF
    newb = (b + ((temp << 7) | (temp >> (32 - 7)))) & 0xFFFFFFFF

    return d, newb, b, c


# MAIN
msg = "hello im theju"

p = padding(msg)
b = getblocks(p)
w = getword(b[0])

A = 0x67452301
B = 0xefcdab89
C = 0x98badcfe
D = 0x10325476

A, B, C, D = md5_round(A, B, C, D, w[0])

print("After 1 round:")
print("A =", hex(A))
print("B =", hex(B))
print("C =", hex(C))
print("D =", hex(D))