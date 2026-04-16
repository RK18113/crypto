def rail_enc(t, rails):
    if rails < 2: return t
    
    fence = [[] for _ in range(rails)]
    r, d = 0, 1
    

    for c in t:
        fence[r].append(c)
        if r == 0: d = 1
        elif r == rails - 1: d = -1
        r += d
        
    return "".join(["".join(row) for row in fence])

def rail_dec(t, rails):
    if rails < 2: return t
    

    n = len(t)
    grid = [[None for _ in range(n)] for _ in range(rails)]
    

    r, d = 0, 1
    for c in range(n):
        grid[r][c] = "*"
        if r == 0: d = 1
        elif r == rails - 1: d = -1
        r += d
    
    


    idx = 0
    for r in range(rails):
        for c in range(n):
            if grid[r][c] == "*" and idx < n:
                grid[r][c] = t[idx]
                idx += 1
                

    res = ""
    print(grid)
    r, d = 0, 1
    for c in range(n):
        res+=grid[r][c]
        if r == 0: d = 1
        elif r == rails - 1: d = -1
        r += d
        
    return res

message = "HELLOWORLD"
n = 3

encrypted = rail_enc(message, n)
decrypted = rail_dec(encrypted, n)

print(f"Encrypted: {encrypted}") 
print(f"Decrypted: {decrypted}")