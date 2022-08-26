import click 
import numpy as np
import rich_click as click 
from src.analyzer import calculateRMSD, calculateKabsch, fullCalculation


click.rich_click.USE_MARKDOWN = True
click.rich_click.STYLE_ERRORS_SUGGESTION = "cyan italic"
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
    
    **Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates. By default the program runs and print the full calculation, i.e. RMSD and Kabsch algorithm. However, you can specify the type of calculation using the options.**
    
    **If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).**
    
    
    """
    if rmsd: 
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        calculateRMSD(f_matrix1, f_matrix2)
    elif kabsch:
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        calculateKabsch(f_matrix1, f_matrix2)
    else: 
        line1, line2 = treatEntry(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separator(line1, line2) 
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        fullCalculation(f_matrix1, f_matrix2)


def treatEntry(filename1, filename2):
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
        msg_exception = ("The length of the coordinates aren't the same.\n"
                        "Please, check your xyz files!")
        raise click.ClickException(msg_exception)
    else:
        return lines1, lines2
    

def separator(list1 = [], list2 = []): 
    #Distinguish atoms from coordinates in both separated arrays
    #Create a list for atoms, and, a list for atomic coordinates
    atom1 = []
    atom2 = []
    coord1 = []
    coord2 = []
    
    for atoms1_pointer in list1:
        if atoms1_pointer.isalpha() == True:
            atom1.append(atoms1_pointer)
        elif atoms1_pointer.isalpha() == False:
            coord1.append(atoms1_pointer)
            
    for atoms2_pointer in list2:
        if atoms2_pointer.isalpha() == True:
            atom2.append(atoms2_pointer)
        elif atoms2_pointer.isalpha() == False:
            coord2.append(atoms2_pointer)

    if (atom1[0] != atom2[0]):
        msg_usgerror = ("The atoms order aren't the same.\n"
                        "Please, check your xyz files!")
        raise click.UsageError(message=msg_usgerror)
    elif (atom1[0] == atom2[0]) and (atom1[1] != atom2[1]):
        msg_usgerror = ("The atoms order aren't the same.\n"
                        "Please, check your xyz files!")
        raise click.UsageError(message=msg_usgerror)
    elif (atom1[0] == atom2[0]) and (atom1[2] != atom2[2]):
        msg_usgerror = ("The atoms order aren't the same.\n"
                        "Please, check your xyz files!")
        raise click.UsageError(message=msg_usgerror)
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
    shape_mtx1 = (row_mtx1, 3)
    shape_mtx2 = (row_mtx2, 3) 
    matrix1 = mtx1.reshape(shape_mtx1)
    matrix2 = mtx2.reshape(shape_mtx2)
    
    return matrix1, matrix2
    

if __name__ == '__main__':
    inputFiles() 
    
    
    



    
    
    

