def hill(t, k):
    t = t.upper().replace(" ", "")
    if len(t) % 2 != 0: t += "X"  
    
    result = ""
    for i in range(0, len(t), 2):
        t1 = ord(t[i]) - ord("A")
        t2 = ord(t[i+1]) - ord("A") 
        
        c1 = (k[0][0] * t1 + k[0][1] * t2) % 26
        c2 = (k[1][0] * t1 + k[1][1] * t2) % 26
        
        result += chr(c1 + ord("A")) + chr(c2 + ord("A"))
        
    return result

m = 'HELP'
k = [[3, 3], [2, 5]] 
ki = [[15, 17], [20, 9]] 

op = hill(m, k)
print(f'Encrypted: {op}')     
print(f'Decrypted: {hill(op, ki)}') 
