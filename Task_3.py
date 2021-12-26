import os


def create_combined_list(directory):

    path = os.listdir(str(directory))
    combined_list = []

    for file in path:
        with open(directory + "/" + file) as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+') as new_file:
        for file in create_combined_list(directory):
            new_file.write(f'File name: {file[0]}\n')
            new_file.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                new_file.write(string + '\n')
            new_file.write('-------------------\n')


create_file_from_directory('text', 'combined_text')



