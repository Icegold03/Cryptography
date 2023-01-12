''' This script is a reference for the math perfomed in the DH Key Exchange
'''
import math

g = 5
p = 25 # Prime number

# Private key a
a = 4 
# Private key b
b = 3 

# Public key A
A = (g**a) % p # A = (5 ^ 4) % 23 = 4
# Public key B
B = (g**b) % p # B = (5 ^ 3) % 23 = 10

# Secret key shared between person a and person b
As = (B**a) % p
Bs = (A**b) % p

print (f"As: {As} | Bs: {Bs}")