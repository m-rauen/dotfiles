from rich.console import Console
from rich.markdown import Markdown

console = Console()

title = """ # COORDINATES ANALYZER"""

msg = """Python CLI program that mathematically compares 2 different molecular structures based on their atomic coordinates. By default the program runs and print the full calculation, i.e. RMSD and Kabsch algorithm, on a external .xyz file generated. However, you can specify the type of calculation using the options.    

If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).

- Result: 

"""

kabsch_msg = """

Rotation matrix generated at: 'rotation_matrix.xyz';\n
Matrix P rotated into Q generated at: 'P_rotated.xyz'.
"""

result_title = Markdown(title)
result_msg = Markdown(msg)

def output_fullResults(rmsd, rotat_mtx, rotat_P_mtx, atoms):
    kabsch_msg = """
    Rotation matrix generated at: 'rotation_matrix.xyz';\n
    P matrix rotated into Q matrix generated at: 'P_rotated.xyz'.
    """
    
    out_rotationMtx = open('rotation_matrix.xyz', 'w')
    out_rotationMtx.write(str(len(rotat_mtx)) + '\n')
    out_rotationMtx.write('RMSD = ' + str(rmsd) + '\n')
    for rotation_elemnts in rotat_mtx: 
        out_rotationMtx.write(str(rotation_elemnts).replace('[','').replace(']',''))
        out_rotationMtx.write('\n')
    
    out_P_rotated = open('P_rotated.xyz', 'w')
    out_P_rotated.write(str(len(rotat_P_mtx)) + '\n')
    out_P_rotated.write('RMSD = ' + str(rmsd) + '\n')
    for rotatedp_elemnts in range(0, len(rotat_P_mtx)):
        out_P_rotated.write(str(atoms[rotatedp_elemnts]) + '    ')  
        out_P_rotated.write(str(rotat_P_mtx[rotatedp_elemnts]).replace('[','').replace(']',''))
        out_P_rotated.write('\n')
        
    console.print(result_title)
    console.print(result_msg, style='bold dim', soft_wrap=False) 
    console.print(kabsch_msg, style='bold white', soft_wrap=False)


def output_onlyRMSD(rmsd):
    msg_rmsd = """
    - RMSD = {} 
    """.format(rmsd)
    console.print(result_title)
    console.print(result_msg, style='bold dim', soft_wrap=False)
    console.print(msg_rmsd, style='bold white')

    
def output_onlyKabsch(rotat_mtx, rotat_P_mtx, atoms):
    out_rotationMtx = open('rotation_matrix.xyz', 'w')
    out_rotationMtx.write(str(len(rotat_mtx)) + '\n')
    out_rotationMtx.write('No RMSD calculated to add here')
    for rotation_elemnts in rotat_mtx: 
        out_rotationMtx.write(str(rotation_elemnts).replace('[','').replace(']',''))
        out_rotationMtx.write('\n')
        
    out_P_rotated = open('P_rotated.xyz', 'w')
    out_P_rotated.write(str(len(rotat_P_mtx)) + '\n')
    out_P_rotated.write('No RMSD calculated to add here')
    for rotatedp_elemnts in range(0, len(rotat_P_mtx)):
        out_P_rotated.write(str(atoms[rotatedp_elemnts]) + '    ')  
        out_P_rotated.write(str(rotat_P_mtx[rotatedp_elemnts]).replace('[','').replace(']',''))
        out_P_rotated.write('\n')
    
    
        
    
  
    
    
    
    
    





    