import click

def length_exception():
    try:
        if len(lines1) != len(lines2):
            msg_exception = ("The length of the coordinates aren't the same.\n"
                        "Please, check your xyz files!")
            raise click.ClickException(msg_exception)
    except Exception as clic
    
    msg_exception = ("The length of the coordinates aren't the same.\n"
                        "Please, check your xyz files!")
    raise click.ClickException(msg_exception)

def atoms_exception():
    msg_usgerror = ("The atoms order aren't the same.\n"
                        "Please, check your xyz files!")
    raise click.UsageError(message=msg_usgerror)

def mtxrow_exception():
    msg_exception = ("")
    raise click.ClickException(msg_exception)

