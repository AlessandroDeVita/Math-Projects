from sympy import *

inp = input("What do you want to do? ")

x = symbols('x')
var = symbols('y')
f = exp(sin(x**3)) + ln(1/tan(1/3*x**4))
g = x**var
h = x**2 

def calcolo_derivata(f):
    derivata = diff(f,x)
    print(derivata)

def calcolo_derivata_parziale(g, var):
    derivata_parziale = diff(g, var)
    print(derivata_parziale)

def calcolo_valore_derivata(h):
    derivata = diff(h,x)
    valore_derivata = derivata.subs(x, 3)
    print(valore_derivata)

if inp == "derivata":
    calcolo_derivata(f)
elif inp == "derivata parziale":
    calcolo_derivata_parziale(g, var)
elif inp == "valore derivata":
    calcolo_valore_derivata(h) 





