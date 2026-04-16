import random

p, q, g = 47, 23, 2

def sign(h, x):
    k = random.randint(1, q-1)
    
    r = pow(g, k, p) % q
    ki = pow(k, -1, q)
    
    s = (ki * (h + x*r)) % q   
    
    return r, s

def verify(s, h, r, y):
    w = pow(s, -1, q)
    
    u1 = (h * w) % q   
    u2 = (r * w) % q   
    
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    
    return "valid" if v == r else "invalid"

# test
x = 10
y = pow(g, x, p)

r, s = sign(7, x)
print(verify(s, 7, r, y))