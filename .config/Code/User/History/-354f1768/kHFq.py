import numpy as np
from error.exceptions import *

def treat_xyz(filename1, filename2):
    #Treat lines (separate) of both arrays
    lines1 = [] 
    lines2 = []
    for first_pointer in filename1:
        for line in first_pointer.strip().split(): 
            lines1.append(line)
            
    for second_pointer in filename2: 
        for line in second_pointer.strip().split():
            lines2.append(line)

    if len(lines1) != len(lines2):
        length_exception()
    else:
        return lines1, lines2
    

def separate_xyz(list1 = [], list2 = []): 
    #Distinguish atoms labels from coordinates in both separated arrays
    atom1 = []
    atom2 = []
    coord1 = []
    coord2 = []
    
    for atoms1_pointer in list1:
        if atoms1_pointer.isalpha() == True:
            atom1.append(atoms1_pointer)
        elif atoms1_pointer.isalpha() == False:
            #coord1.append(atoms1_pointer)
            print(atoms1_pointer)
            
    for atoms2_pointer in list2:
        if atoms2_pointer.isalpha() == True:
            atom2.append(atoms2_pointer)
        elif atoms2_pointer.isalpha() == False:
            coord2.append(atoms2_pointer)

    if (atom1[0] != atom2[0]):
        atoms_exception()
    elif (atom1[0] == atom2[0]) and (atom1[1] != atom2[1]):
        atoms_exception()
    elif (atom1[0] == atom2[0]) and (atom1[1] == atom2[1]) and (atom1[2] != atom2[2]):
        atoms_exception()
    else:
        return atom1, coord1, atom2, coord2        
    

def format_xyz(arr_coords1 = [], arr_coords2 = [], arr_atoms1 = [], arr_atoms2 = []):
    #Convert to float and transform array to matrix 
    mtx1 = np.array(arr_coords1, dtype='float64')
    mtx2 = np.array(arr_coords2, dtype='float64')
    matrix1 = np.asmatrix(mtx1)
    matrix2 = np.asmatrix(mtx2)
    
    #Create the shape and generate both matrices
    row_mtx1 = len(arr_atoms1)
    row_mtx2 = len(arr_atoms2)
    if (row_mtx1) != (row_mtx2):
        mtxrow_exception()
    else:
        shape_mtx1 = (row_mtx1, 3)
        shape_mtx2 = (row_mtx2, 3) 
        matrix1 = mtx1.reshape(shape_mtx1)
        matrix2 = mtx2.reshape(shape_mtx2)
    
    return matrix1, matrix2