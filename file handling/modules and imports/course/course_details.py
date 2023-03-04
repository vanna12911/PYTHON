import os, sys
from os.path import dirname , join , abspath

sys.path.insert(0 , abspath(join(dirname(__file__) , '..')))


# this above whole code creates a pycache file, which enables
#  this program to import evrythinng from the other program , to run their functions in this proogram

from payments import payment_details

def course_here():
    print("this is my course")



payment_details.payments_here()