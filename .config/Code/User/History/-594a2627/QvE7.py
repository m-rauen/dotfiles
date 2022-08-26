import click as clk 

@clk.command()
@clk.option()
def Testing():
    clk.echo('hello world')
    
if __name__ == '__main__':
    exit(Testing()) 
    
    
    



    
    
    

