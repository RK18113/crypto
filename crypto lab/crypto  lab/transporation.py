#tranportation
import math

def enc(k, t):
    n = len(k)

    pl = (n - (len(t) % n)) % n
    t += 'X' * pl
    
    col = [""] * n
   
    for i, c in enumerate(t):
        col[i % n] += c
    
    
    return "".join(col[i-1] for i in k)

def dec(k, t):
    n = len(k)
    rows = len(t) // n

    chunks = [t[i:i + rows] for i in range(0, len(t), rows)]

    ncol = [""] * n
    for i, key_val in enumerate(k):
        ncol[key_val - 1] = chunks[i]

    pt = ""
    for i in range(rows):
        for j in range(n):
            pt += ncol[j][i]
            
    return pt 

# --- TEST ---
t = "HELLO"
k = [4, 1, 2, 3] 
op = enc(k, t)
print(f"Encrypted: {op}")
print(f"Decrypted: {dec(k, op)}")