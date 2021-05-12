from typing import Tuple
import json


def write_line(file_name: str, line_for_write: str):
    if not line_for_write or not isinstance(line_for_write, str):
        return False
    with open(file_name, 'a') as file:
        file.write(line_for_write)
        print('successfully write')
    return True


def write_lines(file_name: str, lines_for_write: Tuple):
    if not lines_for_write or not isinstance(lines_for_write, Tuple):
        return False
    with open(file_name, 'a') as file:
        file.writelines(lines_for_write)
        print('successfully write')
    return True


def replace_numbers(file_to_read: str, file_to_write: str):
    lines_to_write = []
    with open(file_to_read) as f_r:
        all_lines = f_r.readlines()
        for line in all_lines:
            new_line = ''
            for char in line:
                if char == '0':
                    new_line += '1'
                elif char == '1':
                    new_line += '0'
                else:
                    new_line += char
            lines_to_write.append(new_line)

    with open(file_to_write) as f_w:
        f_w.writelines(file_to_write)


# write_line(file_name='test_file_1.txt', line_for_write='aaa\n')
# write_lines(file_name='test_file_1.txt', lines_for_write=('some line\n', 'some line\n'))

some_dict = {
    'some key': None
}
with open('some_file.json', 'a') as some_file:
    data = json.dumps(some_dict)
    some_file.write(data)
