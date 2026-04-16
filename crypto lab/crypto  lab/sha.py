def rotr(x,n):
    return ((x>>n)|(x<<(64-n))) & 0xFFFFFFFFFFFFFFFF
            
def shr(x,n):
    return x>>n

def sigma0(x):
    return rotr(x,1) ^ rotr(x,8) ^ shr(x,7)

def sigma1(x):
    return rotr(x,19) ^ rotr(x,61) ^ shr(x,6)

def tobinary(m):
    return "".join(format(ord(i),'08b') for i in m)

def padding(msg):
    b = tobinary(msg)
    ol = len(b)
    
    b += '1'
    
    while (len(b)+128) % 1024 != 0:
        b += '0'
    
    b += format(ol,'0128b')
    
    return b

def getword(block):
    w = []
    for i in range(0, 1024, 64):
        w.append(int(block[i:i+64],2))
    return w

def genw16(words):
    return (sigma1(words[14]) + words[9] + sigma0(words[1]) + words[0]) & 0xFFFFFFFFFFFFFFFF


# MAIN
text = "hello this is theju"

p = padding(text)
block = p[:1024]   # IMPORTANT

w = getword(block)

print(genw16(w))