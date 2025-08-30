import bcrypt
import itertools
import string

# The bcrypt hash you gave
hash_str = b"$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"

# Normalize bcrypt identifier ($2y$ → $2b$ for Python's bcrypt lib)
hash_norm = hash_str.replace(b"$2y$", b"$2b$")

# Define the candidate alphabet and length
alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
length = 4

for candidate_tuple in itertools.product(alphabet, repeat=length):
    candidate = "".join(candidate_tuple).encode()

    if bcrypt.checkpw(candidate, hash_norm):
        print("FOUND:", candidate.decode())
        break
