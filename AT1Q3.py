#question 3
#saved as AT1Q3.py
#load module sys
import sys
#Make first command argument in integer type, assign it as variable a
a=int(sys.argv[1])
if a%4!=0:
        print('False')
elif a%100!=0:
        print('True')
elif a%400!=0:
        print('False')
else :
        print('True')
