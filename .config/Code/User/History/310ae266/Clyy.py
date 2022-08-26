import click as clk

from analyzer import readXYZ

#TODO: receive filenames as parameters (coords-analyze --full filename1.xyz filename2.xyz)✅  
#TODO: format text in the terminal✅

@clk.command()
@clk.argument('fname1', type=clk.File('r'))

#⚠ 
#if the options are comments, then, it runs normally
#if the options are implemented here, then it don't run 
#I believe that I have to declare the options in the Testinbg() function

#@clk.option('--full', help='Run and print full calculation (RMSD + Kabsch)')
#@clk.option('--R', help='Run  and print only RMSD calculation')
#@clk.option('--K', help='Run and print only Kabsch calculation')
#⚠ 

def Testing(fname1):
    """
    COORDINATES ANALYZER\n

    A Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.
   
    * Mathematical Methods *
    
    -> RMSD;
    
    -> Kabsch algorithm.
    """
    lines = [] 
    for pointer in fname1:
        for line in pointer.strip().split(): 
            lines.append(line)
    clk.echo(lines) 
        
    #readXYZ(fname1)

# @clk.argument('fname1', type=clk.Path(exists=True))
# #@clk.argument('fname2', type=clk.Path(exists=True))
# def catchFiles(filename1):
#     readXYZ(filename1)
    
    
if __name__ == '__main__':
    Testing() 
    
    
    



    
    
    

