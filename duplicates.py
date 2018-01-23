from os import walk
import sys
from os.path import realpath, getsize, join
from collections import defaultdict


def get_files(directory_path):
    file_list = defaultdict(list)
    for file_path, _, file_names in walk(directory_path):
        for file_name in file_names:
            directory_path = realpath(join(file_path, file_name))
            file_list[
                '{} // Size: {} bytes'.format(
                    file_name,
                    getsize(directory_path)
                )
            ].append(directory_path)
    return file_list


def get_duplicates(file_list):
    duplicates_list = {}
    for file_key, path_list in file_list.items():
        path_list = set(path_list)
        if len(path_list) > 1:
            duplicates_list[file_key] = path_list
    return duplicates_list


def show_duplicates(duplicates_list):
    for file_name, file_paths in duplicates_list.items():
        number_of_duplicates = len(file_paths)
        print ('\n\tFile name: {} // Number of duplicates: {} '.format(
            file_name,
            number_of_duplicates
        ))
        print ('\tPaths:')
        for file_path in file_paths:
            print ('\t{}'.format(file_path))


if __name__ == '__main__':
    try:
        file_list = get_files(sys.argv[1])
        show_duplicates(get_duplicates(file_list))
    except IndexError:
        print ('\n\tSpecify the path to the directory')



