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

def catchFiles(fl_a, fl_b):
    coord_a = np.genfromtxt('./' + fl_a)
    coord_b = np.genfromtxt('./' + fl_b)
    
    # print(arr_a)

path = goTo_dir()
file_a = str(input('Enter file A name: '))
file_b = str(input('Enter file B name: '))
catchFiles(file_a, file_b)





    
    
    

