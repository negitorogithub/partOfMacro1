import os.path
import glob
from typing import TextIO
import sys
import pyperclip


def main():
    # absolute_root_file_path = sys.argv[1]
    absolute_root_file_path = input('親ファイルの絶対パスを入力してください')

    absolute_root_folder_path = os.path.dirname(absolute_root_file_path)
    all_file_absolute_path_list = glob.glob(absolute_root_folder_path + '/*.dart')
    assert all_file_absolute_path_list.count(absolute_root_file_path) == 1
    text_2_copy = ''
    for file_path in all_file_absolute_path_list:
        if file_path == absolute_root_file_path:
            continue
        if add_partof(file_path, absolute_root_file_path):
            print('part \'' + os.path.basename(file_path) + '\';')
            text_2_copy.join('part \'' + os.path.basename(file_path) + '\';\\n')
    pyperclip.copy(text_2_copy)


def add_partof(file_path, absolute_root_file_path):
    with open(file_path, mode='r+') as stream:
        lines = stream.readlines()

    # すでに追加されている
    if lines[0].startswith('part of'):
        return False

    lines.insert(0, 'part of \'' + os.path.basename(absolute_root_file_path) + '\';' +
                 '''
''')
    print(lines[0])
    print(lines[1])
    for line in lines:
        if line.startswith('import '):
            print(line)
    lines = [line for line in lines if not line.startswith('import ')]

    with open(file_path, mode='w')as f:
        f.writelines(lines)
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
