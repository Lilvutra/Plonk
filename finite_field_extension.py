#Finite field extension
#A blueprint for it

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List



F = TypeVar("F") #Generic[F]

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    def __repr__(self):
        return f"Polynomial({self.coeffs})"
    

class IrreduciblePolynomial(ABC, Generic[F]):
    @abstractmethod 
    def modulus() -> Polynomial:
        """Returns the irreducible polynomial used for the field extension."""
        pass

#Example of a specific irreducible polynomial for GF(2^3)
class GF8Poly(IrreduciblePolynomial[int]):
    @staticmethod 
    def modulus() -> Polynomial:
        