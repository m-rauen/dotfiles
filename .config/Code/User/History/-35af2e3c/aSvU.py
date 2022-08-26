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

def catchFiles()
file_a = str(input('Enter file A name: '))
arr_a = np.genfromtxt('./' + file_a)
print(arr_a)




# reference_inp = np.genfromtxt('./CuC72N5H89O3Cl.xyz')
# print(reference_inp)



    
    
    

