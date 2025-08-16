
1. Group → ECC (Elliptic Curve Cryptography)
In ECC, the “points” on the elliptic curve form a group under a special addition rule.

Operation: point addition 

P+Q=R

Identity: the “point at infinity” O

Inverse: the point reflected over the x-axis (undoes addition)

Why a group works: You only need one operation to do discrete log stuff:

Given P and kP, find k → hard problem.

2. Ring → RSA (modular arithmetic)
Integers modulo n form a ring 𝑍n.

You have both addition and multiplication modulo 𝑛


Not every element has a multiplicative inverse (e.g., anything not coprime to 
𝑛 can’t be inverted).

Why a ring works: In RSA, we pick an exponent 
𝑒 and compute 𝐶 = M^𝑒 mod 𝑛

The structure of the ring makes this work, but it’s not a field since 
𝑛 is composite.

3. Field → AES (Galois Fields)
AES math happens in GF(2⁸) — a finite field.

Addition = XOR

Multiplication = polynomial multiplication mod an irreducible polynomial

Every nonzero byte has a multiplicative inverse → that’s why the AES S-box can compute 𝑥^-1 easily.

Why a field works: Fields let you divide (find inverses) which is crucial for mixing and diffusion.

💡 Quick analogy:

Group: You have one reversible action (like walking forward/back on a number line).

Ring: You have two actions (add & multiply), but multiplication might not always be reversible.

Why a field works: Fields let you divide (find inverses) which is crucial for mixing and diffusion.

💡 Quick analogy:

Group: You have one reversible action (like walking forward/back on a number line).

Ring: You have two actions (add & multiply), but multiplication might not always be reversible.

Field: You have two actions and both are always reversible (except multiplying by 0).