import click

def length_exception():
    msg_exception = ("The length of the coordinates aren't the same.\n"
                        "Please, check your xyz files!")
    raise click.ClickException(msg_exception)

def 