#saved as AT1Q6.py
#import math
from math import *
#let the user to input principal, interest rate, and time
P=float(input('Principal P:'))
r=float(input('annual interest rate r:'))
t=float(input('number of years:'))
#return to the output
print(P*e**(r*t))
