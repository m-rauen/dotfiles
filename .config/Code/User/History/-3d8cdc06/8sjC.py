import click
from cli.main import inputFiles

def length_exception():
    msg_exception = ("The length of the coordinates aren't the same.\n"
                    "Please, check your xyz files!")
    raise click.ClickException(msg_exception)

def atoms_exception():
    msg_usgerror = ("The atoms order aren't the same.\n"
                    "Please, check your xyz files!")
    raise click.UsageError(message=msg_usgerror)

def mtxrow_exception():
    msg_exception = ("The generated matrices aren't in the same order\n"
                     "Please, check your xyz files!")
    raise click.ClickException(msg_exception)

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

