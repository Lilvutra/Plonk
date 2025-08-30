from dataclasses import dataclass
from typing import Optional

#Finite Field element(mod p)


class FiniteFieldElement:
    def __init__(self, value: int, p: int):
        if not (0 <= value < p):
            raise ValueError(f"Value {value} is not in the field GF({p})")
        self.value = value
        self.p = p

    def __add__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        if self.p != other.p:
            raise ValueError("Cannot add elements from different fields")
        return FiniteFieldElement((self.value + other.value) % self.p, self.p)

    def __sub__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        if self.p != other.p:
            raise ValueError("Cannot subtract elements from different fields")
        return FiniteFieldElement((self.value - other.value) % self.p, self.p)

    def __mul__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        if self.p != other.p:
            raise ValueError("Cannot multiply elements from different fields")
        return FiniteFieldElement((self.value * other.value) % self.p, self.p)

    def __truediv__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        if self.p != other.p:
            raise ValueError("Cannot divide elements from different fields")
        return FiniteFieldElement((self.value * pow(other.value, self.p - 2, self.p)) % self.p, self.p)

class EllipticCurve:
    def __init__(self, a: int, b: int, p: int):
        self.a = a # Coefficient a of the elliptic curve
        self.b = b # Coefficient b of the elliptic curve
        self.p = p
        
    def is_point_on_curve(self, x: int, y: int) -> bool:
        """Check if the point (x, y) lies on the elliptic curve."""
        return (y * y) % self.p == (x*x*x + self.a * x + self.b) % self.p

class Point:
    def __init__(self, x: int, y: int, curve: EllipticCurve):
        self.x = x
        self.y = y
        self.curve = curve
    
    def __post_init__(self):
        if self.x is None or self.y is None:
            return  # This is the point at infinity
        if not self.curve.is_point_on_curve(self.x, self.y):
            raise ValueError(f"Point ({self.x}, {self.y}) is not on the curve")
        
    def is_point_at_infinity(self) -> bool:
        return self.x is None and self.y is None