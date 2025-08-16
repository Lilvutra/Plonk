#Construct Galois Field 
#Galois Field is a finite field, which means it has a finite number of elements.
#It is denoted as GF(p^n) where p is a prime number and n is a positive integer.
#In this implementation, we will create a Galois Field with integer elements.
#We will implement addition, multiplication, and inverse operations in the Galois Field.
#This is useful in cryptography, error correction codes, and other applications.

# With integer 

class int_galois_field:
    def _init_ (self, p):
        self.p = p
        self.field_size = p 
        self.elements = [i for i in range(p)]
    
    def add(self, a, b):
        return (a+b) % self.p
    
    def multiply(self, a, b):
        return (a*b) % self.p
    
    def inverse(self, a):
        if a == 0:
            raise ValueError("Inverse does not exist for zero in Galois Field")
        return pow(a, self.p - 2, self.p)

class poly_galois_field:
    def __init__(self, p):
        self.p = p
        self.field_size = p
        self.elements = [i for i in range(p)]
        
    def add_poly(self, poly1, poly2):
        max_len = max(len(poly1), len(poly2))