import math
import hashlib

p = 4007
q = 2003
g = 4

x = 1234
msg = "Alice's Contract"

y = pow(g, x, p)

k = 42
k_inv = pow(k, -1, q)

hashmsg_hex = hashlib.sha256(msg.encode('utf-8')).hexdigest()
hashmsg = int(hashmsg_hex, 16) % q

r = pow(g, k, p) % q

s = k_inv * (hashmsg + x*r) % q

s_inv = pow(s, -1, q)

w = s_inv % q

u1 = (hashmsg * w) % q

u2 = (r*w) % q

v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

print("signature valid") if v == r else print("signature invalid")
