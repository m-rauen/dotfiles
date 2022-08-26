import math as mt 
import numpy as np 
import scipy as sp
import os as os 


def goTo_dir():
    home = str(os.path.expanduser('~'))
    print(home)
    dir = str(input("Enter directory name: ")).rstrip().lstrip()
    os.chdir(home + '/' + dir + '/')
    dir_path = os.getcwd() 
    return dir_path 

def catchFiles(fl_a):
    coord_a = np.genfromtxt('./' + fl_a)
    # coord_b = np.genfromtxt('./' + fl_b)

    
    print(coord_a)




path = goTo_dir()
file_a = str(input('Enter file A name: ')) + '.xyz'
# file_b = str(input('Enter file B name: ')) + '.xyz'
catchFiles(file_a)





    
    
    

