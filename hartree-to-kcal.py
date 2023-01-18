fname = input('File name: ')

energy_data = {}
count = 1

for lines in open(fname):
    if lines is None:
        quit()
    else:
        energy = float(lines)
        new_energ = round(energy * 627.50, 3)
        energy_data.update({count:new_energ})
        count += 1

fhandler = open('conv-results.dat', 'w')        
for k,v in energy_data.items():
    fhandler.write(str(k) + '   ' + str(v))
    fhandler.write('\n')
    
print('Everything done!\n'
      'Enjoy your data :)')

