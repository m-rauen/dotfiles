import os
import traceback

fname = input('File name: ')

energy_data = []

while True:
    try:
        if (os.stat(fname).st_size == 0):
            raise IOError('File empty error!')
        else:
            break
    except IOError:
        print("""
              ***************************
              ERROR: Empty file selected!
              ***************************
              """)
        quit()

for lines in open(fname):
    if lines is None:
        try:
            raise ValueError('Empty line error!')
        except ValueError:
            continue
    else:
        new_lines = lines.rstrip()
        words = new_lines.split()
        for w in words:
            if (w.isalpha() == True):
                try:
                    raise ValueError('Words error!')
                except ValueError:
                    continue
            else:  
                try:
                    energy = float(w)
                    conv_energy = (energy * 627.50)
                    energy_data.append(conv_energy)
                except ValueError:
                    energy_data.append(w)
                
fhandler = open('converted_results.dat', 'w')        
for e in energy_data:
    fhandler.write(str(e))
    fhandler.write('\n')
    
print('All done!\n'
      'Enjoy your data :)')

