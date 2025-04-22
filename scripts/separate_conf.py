def extract_first_n_conformers(input_file, limit, output_file='selected_conformers.xyz'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    line_index = 0  
    conf_index = 0

    with open(output_file, 'w') as out:
        while line_index < len(lines) and conf_index < limit:
            try:
                num_atoms = int(lines[line_index].strip())
                comment_line = lines[line_index + 1]
                coordinates = lines[line_index + 2 : line_index + 2 + num_atoms]

                if len(coordinates) != num_atoms:
                    print(f'Skipping incomplete block at line {line_index}')
                    break

                out.write('{}\n'.format(num_atoms))
                out.write('conformer{} -> '.format(conf_index) + comment_line)
                out.writelines(coordinates)

                conf_index += 1
                line_index += 2 + num_atoms
            except ValueError:
                pass

    print('✅ Saved first {} conformers to {}'.format(conf_index, output_file))
 
filename, limit = input('Enter filename and limit (file.xyz,int): ').split(',')
filename = str(filename)
limit = int(limit)
extract_first_n_conformers(filename, limit)