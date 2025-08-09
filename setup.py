# Implement setup for Plonk: https://www.inevitableeth.com/home/concepts/pcs-trusted-setup
# we want to hide a secret number S
# we generate points by repeatedly multiplying S with itself and applying our elliptic curve function
# the specific points - related by S - are indistinguishable from random data
# the true value of S is destroyed and lost, forever
# create elliptic curve points
# G1 curve: y^2 = x^3 + 3


