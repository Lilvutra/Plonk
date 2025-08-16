# RSA naive implementation
import random
import math

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False 
    return True 


def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime

# Iteration approach to find modular inverse
# This is a simple brute-force method, not efficient for large numbers
# For larger numbers, use Extended Euclidean Algorithm or Fermat's Little Theorem
# Here we assume e is small and phi is large enough to find an inverse
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("No modular inverse found")

p, q = generate_prime(100, 200), generate_prime(100, 200)

while p == q:
    q = generate_prime(100, 200)

# the modulus n which is part of both the public and private keys
n = p * q 
print("n (modulus):", n)

#calculate phi(n), Euler's totient function
phi_n = (p-1) * (q-1)

# e is the public exponent, while d is the private exponent and is the modular inverse of e mod phi(n)
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)

d = mod_inverse(e, phi_n)

m = "Hello, RSA"

m_encoded = [ord(char) for char in m]   
print("Encoded message:", m_encoded)

#m ^ e mod n = char
ciphertext = [pow(char, e, n) for char in m_encoded] # char^e mod n
print("Ciphertext:", ciphertext)

m_decoded = [pow(char, d, n) for char in ciphertext]  # char^d mod n
m_decoded = ''.join(chr(char) for char in m_decoded)

print("Decoded message:", m_decoded)
print("Public key (n, e):", (n, e))
print("Private key (n, d):", (n, d))