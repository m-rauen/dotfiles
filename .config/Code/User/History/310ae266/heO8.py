import click as clk
from analyzer import formatXYZ

#TODO: treat clk.option into Testing(); 

@clk.command()
@clk.argument('fname1', type=clk.File('r'))        
@clk.argument('fname2', type=clk.File('r'))

#⚠ 
#if the options are comments, then, it runs normally
#if the options are implemented here, then it don't run 
#I believe that I have to declare the options in the Testinbg() function

#@clk.option('--full', help='Run and print full calculation (RMSD + Kabsch)')
#@clk.option('--R', help='Run  and print only RMSD calculation')
#@clk.option('--K', help='Run and print only Kabsch calculation')
#⚠ 

def Testing(fname1, fname2): 
    """
    COORDINATES ANALYZER\n

    A Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.
   
    * Mathematical Methods *
    
    -> RMSD;
    
    -> Kabsch algorithm.
    """
    lines1 = [] 
    lines2 = []
    for first_pointer in fname1:
        for line in first_pointer.strip().split(): 
            lines1.append(line)
            
    for second_pointer in fname2: 
        for line in second_pointer.strip().split():
            lines2.append(line)
    
    formatXYZ(lines1, lines2)

    
if __name__ == '__main__':
    Testing() 
    
    
    



    
    
    

