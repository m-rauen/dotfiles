import rich_click as click 

from src.analyzer import *
from src.treatment import *
from error.exceptions import *


click.rich_click.USE_MARKDOWN = True


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
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        calculateKabsch(f_matrix1, f_matrix2, arr_label_atoms)
    else: 
        line1, line2 = treat_xyz(fname1, fname2)
        atoms1, coords1, atoms2, coords2 = separate_xyz(line1, line2) 
        for c in atoms1:
            arr_label_atoms.append(c)
        f_matrix1, f_matrix2 = format_xyz(coords1, coords2, atoms1, atoms2)
        fullCalculation(f_matrix1, f_matrix2, arr_label_atoms)
       
   
   

if __name__ == '__main__':
    inputFiles() 
    
    
    



    
    
    

