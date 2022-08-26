import numpy as np 
import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box 


console = Console()
msg = """
# COORDINATES ANALYZER

Python CLI program that mathematically compare 2 sets of molecular structures, based on their atomic coordinates, throughout the Root-Mean-Square Deviation, and, Kabsch algorithm. If you are interested in the source code, you can find it on my [**Github**](https://github.com/m-rauen/Coordinates_Analyzer).
"""

result_msg = Markdown(msg)

def output_fullResults():
    print('hello world')


def output_onlyRMSD(rmsd):
    msg_rmsd = """
    - RMSD = {}
    """.format(rmsd)
    console.print(result_msg, soft_wrap=False)
    result_rule = console.rule('[bold cyan]Results')
    console.print(msg_rmsd)
    
def output_onlyKabsch(rotat_mtx, rotat_P_mtx):
    msg_kabsch = """
    - Rotational: 
    """
    console.print(result_msg, soft_wrap=False)
    result_rule = console.rule('[bold blue] Results')
    console.print(msg_kabsch)
    np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    print('\n {} \n'
          .format(np.matrix(rotat_mtx)))
    
    for rotat_elements in rotat_mtx: 
        np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
        print('[' + str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')
        
    
  
    
    
    


    





    