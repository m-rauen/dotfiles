import numpy as np 
import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box 


console = Console()
msg = """
# COORDINATES ANALYZER

Python CLI program that mathematically compare 2 sets of molecular structures, based on their atomic coordinates, throughout the Root-Mean-Square Deviation, and, Kabsch algorithm. If you are interested in the source code, you can find it on my Gith


"""

result_msg = Markdown(msg)

def output_fullResults():
    print('hello world')


def output_onlyRMSD(rmsd):
    msg_rmsd = """
    RMSD = {}
    """.format(rmsd)
    result_msg_rmsd = Markdown(msg_rmsd)
    console.print(result_msg, soft_wrap=False)
    result_rule = console.rule('[bold cyan]Results')
    console.print(result_msg_rmsd)
    
def output_onlyKabsch(rotat_mtx, rotat_P_mtx):
    msg_kabsch = click.wrap_text(
    """
    \n
    COORDINATES ANALYZER\n
    Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    * Results *\n
    """
    , width=78, preserve_paragraphs=True)
    click.echo(msg_kabsch, err=True)
    
    np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    print('Rotational:\n {} \n'
          .format(np.matrix(rotat_mtx)))
    
    # for rotat_elements in rotat_mtx: 
    #     np.set_printoptions(precision=4, formatter={'float': '{:.4f}'.format})
    #     print('[' + str(rotat_elements).replace(']', '').replace('[', ''), end=',\n')
        
    
    # print(f"""
    #           COORDINATES ANALYZER\n 
    #           Python CLI program that mathematically compare 2 different molecular structures based on their atomic coordinates.\n
    #           * Results *\n 
    #           Rotational:\n 
    #           {rotat_elements}
    #           """, end='\n')
    
    
    
    
    
    # print('Rotational:\n {} \n\n'
    #       'P_rotated: \n {}'.format(np.matrix(matrix_R), np.matrix(rot_matrixP)))
    
    
    
#in output_result() we can differentiate results by their type (list = Kabsch // numpy.float64 = RMSD) 
#------------------------------------
# if teste_de_lista == []:
#     print('sepa vai dar boa')
# else:
#     print('sepa n vai dar boa')
#------------------------------------

    





    