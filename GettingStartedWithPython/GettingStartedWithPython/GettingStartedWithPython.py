# Lists test
tst_list = ['test1', 'test2', 3]
for element in tst_list:
    print(element)
del tst_list[1]
for element in tst_list:
    print(element)

# Tuples
tst_tuple = 'element1', 'element2', 'element3'
for element in tst_tuple:
    print(element)

# Dictionary
dictionary = {'key1':'value1','key2':'value2'}
print(dictionary['key1'])
del dictionary['key1']
print (dictionary)

# Set
tst_set = set(['Jane','Mark','Stephen'])
print(tst_set)

# Functions
def f(n):
    return n*2
print()
print(f(2))

def callfunction(f,n):
    return f(n)

print()
print(callfunction(f,1))

def callfunctionsquared(f,n):
    return f(f(n))
print()
print(callfunctionsquared(f,2))

# Classes
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    
    def brake(self):
        print("Braking!")
# Instances
green_bike = Bike("Green", "Steel")
yellow_bike = Bike('Yellow', 'Carbon fiber')

green_bike.brake()

# Easter egg
import this
print()
# Documentation
def square(n):
    """Return the squared number.

    >>> square(2)
    4
    >>> square(4)
    16
    """
    return n*n

print(square(5))
print()
help(square)
# Complex numbers
print()
print("Complex numbers")
c = 1.23 + 4.56j
print(c)
print("Real part of number", c.real)
print("Imaginary part of number", c.imag)
print(c.conjugate())
print(c*2)
print(c ** 2) # power operator
d = 1 + 2.34j
print(c-d)
print()
# Fraction and Decimal
print('Fraction and Decimal numbers')
from fractions import Fraction
frac = Fraction(10,6)
print(frac)
print(frac.denominator)
print(frac.numerator)

from decimal import Decimal as Dec
decim = Dec(3.14) # argument as float
print(decim) 
decim = Dec("3.14") # argument as string
print(decim)