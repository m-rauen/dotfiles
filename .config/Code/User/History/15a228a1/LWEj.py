import click 
import numpy as np
import rich_click as click 

from src.analyzer import *
from src.treatment import *
from error.exceptions import *


click.rich_click.USE_MARKDOWN = True
click.rich_click.STYLE_ERRORS_SUGGESTION = "bold cyan"
click.rich_click.ERRORS_SUGGESTION = "\n Try running 'coords-analyze --help' for more detailed information.\n"
click.rich_click.ERRORS_EPILOGUE = "To find out more about the code, visit https://github.com/m-rauen/Coordinates_Analyzer\n"


@click.command()
@click.argument('fname1', type=click.File('r'))        
@click.argument('fname2', type=click.File('r'))
@click.option('--rmsd',is_flag=True, help='Run and print only RMSD result', default=False)
@click.option('--kabsch', is_flag=True, help='Run and print only Kabsch algorithm results', default=False)
def inputFiles(fname1, fname2, rmsd, kabsch): 
    """
    # COORDINATES ANALYZER
    
    **Python CLI program that mathematically compares 2 different molecular structures based on their atomic coordinates. By default the program runs and print the full calculation, i.e. RMSD and Kabsch algorithm, on a external .xyz file generated. However, you can specify the type of calculation using the options.**
    
    **If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).**
    
    
    """
    if rmsd: 
        line1, line2 = treat_xyz(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separate_xyz(line1, line2) 
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        calculateRMSD(f_matrix1, f_matrix2)
    elif kabsch:
        arr_label_atoms = []
        line1, line2 = treat_xyz(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separate_xyz(line1, line2) 
        for c in atoms1:
            arr_label_atoms.append(c)
        # print(arr_label_atoms)
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        calculateKabsch(f_matrix1, f_matrix2, arr_label_atoms)
    else: 
        line1, line2 = treat_xyz(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separate_xyz(line1, line2) 
        for c in atoms1:
            arr_label_atoms.append(c)
        #print(arr_label_atoms)
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        fullCalculation(f_matrix1, f_matrix2, arr_label_atoms)
        


# def treat_xyz(filename1, filename2):
#     #Treat lines (separate) of both arrays
#     lines1 = [] 
#     lines2 = []
#     for first_pointer in filename1:
#         for line in first_pointer.strip().split(): 
#             lines1.append(line)
            
#     for second_pointer in filename2: 
#         for line in second_pointer.strip().split():
#             lines2.append(line)

#     if len(lines1) != len(lines2):
#         length_exception()
#     else:
#         return lines1, lines2
    

# def separate_xyz(list1 = [], list2 = []): 
#     #Distinguish atoms labels from coordinates in both separated arrays
#     atom1 = []
#     atom2 = []
#     coord1 = []
#     coord2 = []
    
#     for atoms1_pointer in list1:
#         if atoms1_pointer.isalpha() == True:
#             atom1.append(atoms1_pointer)
#         elif atoms1_pointer.isalpha() == False:
#             coord1.append(atoms1_pointer)
            
#     for atoms2_pointer in list2:
#         if atoms2_pointer.isalpha() == True:
#             atom2.append(atoms2_pointer)
#         elif atoms2_pointer.isalpha() == False:
#             coord2.append(atoms2_pointer)

#     if (atom1[0] != atom2[0]):
#         atoms_exception()
#     elif (atom1[0] == atom2[0]) and (atom1[1] != atom2[1]):
#         atoms_exception()
#     elif (atom1[0] == atom2[0]) and (atom1[1] == atom2[1]) and (atom1[2] != atom2[2]):
#         atoms_exception()
#     else:
#         return atom1, coord1, atom2, coord2        
    

# def format_xyz(arr_coords1 = [], arr_coords2 = [], arr_atoms1 = [], arr_atoms2 = []):
#     #Convert to float and transform array to matrix 
#     mtx1 = np.array(arr_coords1, dtype='float64')
#     mtx2 = np.array(arr_coords2, dtype='float64')
#     matrix1 = np.asmatrix(mtx1)
#     matrix2 = np.asmatrix(mtx2)
    
#     #Create the shape and generate both matrices
#     row_mtx1 = len(arr_atoms1)
#     row_mtx2 = len(arr_atoms2)
#     if (row_mtx1) != (row_mtx2):
#         mtxrow_exception()
#     else:
#         shape_mtx1 = (row_mtx1, 3)
#         shape_mtx2 = (row_mtx2, 3) 
#         matrix1 = mtx1.reshape(shape_mtx1)
#         matrix2 = mtx2.reshape(shape_mtx2)
    
#     return matrix1, matrix2
    
    

if __name__ == '__main__':
    inputFiles() 
    
    
    



    
    
    

