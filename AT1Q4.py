#question4 saved as AT1Q4
import random as rd
import sys
#make first and second command argument as integer numbers and assignment them to a and b
a=int(sys.argv[1])
b=int(sys.argv[2])
#check whether b>a
if b>a:
    condion=True
else :
    condion=False
#Ask to put another number if the condition is not met
while not condion:
    b=int(input('put another greater number for the second one:'))
    if b>a:
        condion=True
    else :
        condion=False
#print out the required
print(rd.randint(a,b))
                        
