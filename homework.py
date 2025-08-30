#codeforce problem
import sys 


"""t: number of test cases
a: string
n: length of string a
b,c: string 
m: length of string b,c"""

#Vlad can only append characters to the beginning of string a
#Dima can only add characters to the end of string a

lines = sys.stdin.read().splitlines()
t = int(lines[0])

test_cases = []

for i in range(1, t * 5, 5):
    n = int(lines[i])    
    a = lines[i + 1]
    m = int(lines[i + 2])
    b = lines[i + 3]
    c = lines[i + 4]
    
    #if Vlad, adding char to the beginning
    #if Dima, adding char to the end
    # since python is 
    
    for bla in range(m):
        if c[bla] == 'V':
            a = b[bla] + a
        else:
            a = a + b[bla]
        
    
    test_cases.append((n, a, m, b, c))
    
print(test_cases)




























