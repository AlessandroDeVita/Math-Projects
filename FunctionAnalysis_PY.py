from sympy import *

init_printing(use_unicode=True)
#
var = input("Che cosa vuoi fare? ")
#
x = Symbol('x')
#WRITE IN THE FUNCTION
y = cos(x)/1-2*sin(x)
#ASSIGN THE VALUE OF THE LIMIT
value = oo

def islimit(y,x,value):
    return (limit(y,x,value))

def checkifcontinus(y,x,symbol):
    return (limit(y,symbol,x).is_real)