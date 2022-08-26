import numpy as np
from error.exceptions import *

def convert_labels(elements_nmbrs):
    atomic_number = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Sc": 21,
    "Ti": 22,
    "V": 23,
    "Cr": 24,
    "Mn": 25,
    "Fe": 26,
    "Co": 27,
    "Ni": 28,
    "Cu": 29,
    "Zn": 30,
    "Ga": 31,
    "Ge": 32,
    "As": 33,
    "Se": 34,
    "Br": 35,
    "Kr": 36,
    "Rb": 37,
    "Sr": 38,
    "Y": 39,
    "Zr": 40,
    "Nb": 41,
    "Mo": 42,
    "Tc": 43,
    "Ru": 44,
    "Rh": 45,
    "Pd": 46,
    "Ag": 47,
    "Cd": 48,
    "In": 49,
    "Sn": 50,
    "Sb": 51,
    "Te": 52,
    "I": 53,
    "Xe": 54,
    "Cs": 55,
    "Ba": 56,
    "La": 57,
    "Ce": 58,
    "Pr": 59,
    "Nd": 60,
    "Pm": 61,
    "Sm": 62,
    "Eu": 63,
    "Gd": 64,
    "Tb": 65,
    "Dy": 66,
    "Ho": 67,
    "Er": 68,
    "Tm": 69,
    "Yb": 70,
    "Lu": 71,
    "Hf": 72,
    "Ta": 73,
    "W": 74,
    "Re": 75,
    "Os": 76,
    "Ir": 77,
    "Pt": 78,
    "Au": 79,
    "Hg": 80,
    "Tl": 81,
    "Pb": 82,
    "Bi": 83,
    "Po": 84,
    "At": 85,
    "Rn": 86,
    "Fr": 87,
    "Ra": 88,
    "Ac": 89,
    "Th": 90,
    "Pa": 91,
    "U": 92,
    "Np": 93,
    "Pu": 94,
    "Am": 95,
    "Cm": 96,
    "Bk": 97,
    "Cf": 98,
    "Es": 99,
    "Fm": 100,
    "Md": 101,
    "No": 102,
    "Lr": 103,
    "Rf": 104,
    "Db": 105,
    "Sg": 106,
    "Bh": 107,
    "Hs": 108,
    "Mt": 109,
    "Ds": 110,
    "Rg": 111,
    "Cn": 112,
    "Nh": 113,
    "Fl": 114,
    "Mc": 115,
    "Lv": 116,
    "Ts": 117,
    "Og": 118,
}
    
    atoms = []
    
    for c in elements_nmbrs:
        atoms.append(int(c)) 
        
    for i in atomic_number.keys():
        for j in atoms:
            if i == j:
                print('deu boa')
            else: 
                print('bugou')
                # atoms.append(i.values())
    
            
        

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
    atoms1_numbers = []
    atoms2_numbers = []
    
    # print(list1[:])
    
    for atoms1_pointer in list1:
        if atoms1_pointer.isalpha() == True:
            atom1.append(atoms1_pointer)
        elif atoms1_pointer.isalpha() == False:
            if atoms1_pointer.isdigit() == True:    
                atoms1_numbers.append(atoms1_pointer)
        else: 
            coord1.append(atoms1_pointer)
    if len(atoms1_numbers) != 0:
        convert_labels(atoms1_numbers)
    else: 
        pass
    
            
    for atoms2_pointer in list2:
        if atoms2_pointer.isalpha() == True:
            atom2.append(atoms2_pointer)
        elif atoms2_pointer.isalpha() == False:
            if atoms2_pointer.isdigit() == True:
                atoms2_numbers.append(atoms2_pointer)
        else: 
            coord2.append(atoms2_pointer)
    if len(atoms2_numbers) != 0:
        atom2 = convert_labels(atoms2_numbers)
    else: 
        pass


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