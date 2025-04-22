import re

def get_separated_xyz(ids, file):
    new_ids = []
    index = 0
    with open(file, 'r') as f:
        lines = f.readlines()
    
    for conf_id in ids:
        new_conf_id = 'conformer{}'.format(conf_id)
        new_ids.append(new_conf_id)
        
    while index < len(lines):
        line = lines[index].strip()
        if line.isnumeric() == True:
            num_atoms = int(line)
            header = lines[index + 1].strip()
            for conf_id in new_ids:
                if re.match('^{}\s*->.'.format(conf_id), header):
                    coordinates = lines[index : index + num_atoms + 2]
                    output_file = '{}.inp'.format(conf_id)
                    with open(output_file, 'w') as out:
                        out.write('! b3lyp def2-svp d4 rijcosx autoaux\n')
                        out.write('! cpcm()\n\n')
                        out.write('%maxcore\n\n')
                        out.write('%pal\n')
                        out.write('    nprocs\n')
                        out.write('end\n\n')
                        out.write('* xyz 0 1\n')
                        out.writelines(coordinates[2:])
                        out.write('*')
                    break
            index += num_atoms + 2
        else: 
            index += num_atoms + 2
            pass
        
filename = str(input('Enter filename (out.xyz): ')).strip()
conformer_ids = input('Enter conformer IDs (1,5,10): ').split(',')
get_separated_xyz(conformer_ids, filename)
         
        
