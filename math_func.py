g = 9789
p = 23978

a = 20978
b = 94876

def first(g,p,s):
    return g**s % p

def second(p, s, T):
    return T**s % p


print(second(p,a, first(g,p,b)))
print(second(p,b, first(g,p,a)))