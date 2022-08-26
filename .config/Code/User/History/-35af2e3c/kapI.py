import math as mt 
import numpy as np 
import scipy as sp
import os as os 


def goTo_dir():
    home = str(os.path.expanduser('~'))
    print(home)
    dir = str(input("Enter directory (containing the files) name: "))
    os.chdir(home + '/' + dir + '/')
    dir_path = os.getcwd() 
    return dir_path 
path = goTo_dir()





# reference_inp = np.genfromtxt('./CuC72N5H89O3Cl.xyz')
# print(reference_inp)



    
    
    

