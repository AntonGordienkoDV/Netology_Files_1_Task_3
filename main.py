import os


def list_of_txt(path):
    txt_list = []
    for file_name in os.listdir(path):
        if file_name.endswith('txt'):
            txt_list.append(file_name)
    return txt_list


def read_file(directory: str, name: str):
    file = {'name': name}
    with open(os.path.join(directory, name), encoding='UTF8') as inf:
        file['content'] = inf.readlines()
        file['length'] = len(file['content'])
    return file


def read_all_files(path: str):
    files = []
    file_names_list = list_of_txt(path)
    for file_name in file_names_list:
        files.append(read_file(path, file_name))
    return files


def print_to_file(files: list, output_file_name: str = 'output.txt'):
    sorted_files = sorted(files, key=lambda file_: file_['length'])
    with open(output_file_name, 'w', encoding='UTF8') as ouf:
        for file in sorted_files:
            ouf.write(f'{file["name"]}\n{file["length"]}\n')
            ouf.writelines(file.get('content'))
            ouf.write('\n')


def main():
    path = os.path.join(os.getcwd(), 'Files')
    files = read_all_files(path)
    print_to_file(files)


if __name__ == '__main__':
    main()
