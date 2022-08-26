import rich_click as click

click.rich_click.STYLE_ERRORS_SUGGESTION = "bold cyan"
click.rich_click.ERRORS_SUGGESTION = "\n Try running 'coords-analyze --help' for more detailed information.\n"
click.rich_click.ERRORS_EPILOGUE = "To find out more about the code, visit https://github.com/m-rauen/Coordinates_Analyzer\n"

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