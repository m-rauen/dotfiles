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

def catchFiles(flA, flB):
    arr_a = np.genfromtxt('./' + file_a)
    arr_b = np.genfromtxt('./' + file_b)
    print(arr_a)

path = goTo_dir()
file_a = str(input('Enter file A name: '))
file_b = str(input('Enter file B name: '))
catchFiles(file_a, file_b)

# reference_inp = np.genfromtxt('./CuC72N5H89O3Cl.xyz')
# print(reference_inp)



    
    
    

