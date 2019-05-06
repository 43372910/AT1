#saved as AT1Q5.py
#download module datetime
from datetime import *
import sys
#make first and second arugment as m(month) and d(date)
m=int(sys.argv[1])
d=int(sys.argv[2])
#change the number into date type
date1=date(2018,3,20)
date2=date(2018,6,20)
datetest=date(2018,m,d)
#check the condtion
if date1<datetest<date2:
        print('True')
else :
        print('False')
