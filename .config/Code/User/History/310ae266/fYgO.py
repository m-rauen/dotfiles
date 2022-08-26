import click as clk

from analyzer import readXYZ

#TODO: receive filenames as parameters (coords-analyze --full filename1 filename2) 
#TODO: format text in the terminal

@clk.command()
@clk.option('--full', help='Run and print full calculation (RMSD + Kabsch)')
@clk.option('--R', help='Run  and print only RMSD calculation')
@clk.option('--K', help='Run and print only Kabsch calculation')
def Testing():
    """
    COORDINATES ANALYZER
     
        
    A Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.
   
    * Mathematical Methods *
    
    -> RMSD;
    
    -> Kabsch algorithm.
    """
    catchFiles()

@clk.argument('fname1', type=clk.Path(exists=True))
#@clk.argument('fname2', type=clk.Path(exists=True))
def catchFiles(filename1):
    readXYZ(filename1)
    
    
if __name__ == '__main__':
    exit(Testing()) 
    
    
    



    
    
    

