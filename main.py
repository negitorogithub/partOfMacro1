import os.path
import glob
from typing import TextIO


def main():
    absolute_root_file_path = os.path.abspath(input('親ファイルの絶対パスを入力してください'))
    absolute_root_folder_path = os.path.dirname(absolute_root_file_path)
    all_file_absolute_path_list = glob.glob(absolute_root_folder_path + '/*.dart')
    assert all_file_absolute_path_list.count(absolute_root_file_path) == 1
    for file_path in all_file_absolute_path_list:
        if file_path == absolute_root_file_path:
            continue
        if add_partof(open(file_path, mode='r+'), absolute_root_file_path):
            print('part \'' + os.path.basename(file_path) + '\';')


def add_partof(stream: TextIO, absolute_root_file_path):
    first_line = stream.readline()

    # すでに追加されている
    if first_line.startswith('part of'):
        return False
    stream.write('part of \'' + os.path.basename(absolute_root_file_path) + '\';')
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
