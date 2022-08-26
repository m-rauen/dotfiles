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



