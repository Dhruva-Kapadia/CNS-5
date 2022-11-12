import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

def encrypt(m, e, n):        
    c = pow(m, e)
    c = math.fmod(c, n)
    return c

def decrypt(c, d, n):
    p = pow(c, d)
    p = math.fmod(p, n)
    return p

p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):

    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1

k = 2
d = (1 + (k*phi))/e

msg = 19.0

print("Message data = ", msg)

ciphertext = encrypt(msg, e, n)
print("Encrypted data = ", ciphertext)

plaintext = decrypt(ciphertext, d, n)
print("Original Message = ", plaintext)
