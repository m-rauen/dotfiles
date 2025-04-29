import re

def parse_conformer_ids(raw_input):
    ids = []
    parts = raw_input.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            ids.extend(range(start, end + 1))
        else:
            ids.append(int(part))
    return ids

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
                    output_file = '{}.xyz'.format(conf_id)
                    with open(output_file, 'w') as out:
                        out.writelines('{}\n'.format(num_atoms))
                        out.writelines(header + '\n')
                        out.writelines(coordinates[2:])
                    break
            index += num_atoms + 2
        else: 
            index += num_atoms + 2
            pass
        
filename = str(input('Enter filename (out.xyz): ')).strip()
raw_ids = input('Enter conformer IDs (e.g., 1,5,10-12): ')
conformer_ids = parse_conformer_ids(raw_ids)
get_separated_xyz(conformer_ids, filename)
         
        
