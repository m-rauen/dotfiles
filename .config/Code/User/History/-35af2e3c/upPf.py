import math as mt 
import numpy as np 
import scipy as sp
import os as os 
from pathlib import Path as Pt 

def goTo_dir():
    home = str(os.path.expanduser('~'))
    print(home)
    dir = str(input("Enter directory (containing the files) name: "))
    os.chdir(home + '/' + dir + '/')
    return os.getcwd()

result = goTo_dir()
print(result)



# reference_inp = np.genfromtxt('./CuC72N5H89O3Cl.xyz')
# print(reference_inp)



    
    
    

