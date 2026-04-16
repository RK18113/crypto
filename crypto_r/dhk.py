import math

g = 3
n = 97

a = 5
b = 7

ga = pow(g, a, n)
gb = pow(g, b, n)

gab = pow(gb, a, n)
gba = pow(ga, b, n)

print(f"alice: {gab}, bob: {gba}")


e = 11

ge = pow(g, e, n)

gea = pow(ge, a, n) 
geb = pow(ge, b, n) 

gae = pow(ga, e, n)
gbe = pow(gb, e, n)


print(f"alice: {gea}, bob: {geb}, eve_alice: {gae}, eve_bob: {gbe}")
