import os

"""
Задача_1
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
    записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл"
"""


def average_points(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = [(line.rstrip()).split() for line in file]
    data_dict = {}
    for info in data:
        item = {
            f'{info[1]} {info[0][0]}{"."}': round(sum([float(x) for x in info if x.isdigit()]) / len(info[2:]), 2)
        }
        data_dict.update(item)
    return data_dict


def min_points(input_array: dict) -> str:
    min_point_list = [[key, value] for key, value in input_array.items() if value < 5.0]
    max_len = max([len(min_point_list[i][0]) for i in range(len(min_point_list))]) + 8
    result = ','.join(str(min_point_list[i][0]).ljust(max_len, ' ') + str(min_point_list[i][1]) + '\n'
                      for i in range(len(min_point_list))).replace(',', '')
    return result


def create_file(input_array: dict, file_path: str) -> None:

    with open(file_path, 'w') as file:
        for key, val in input_array.items():
            max_len = max([len(key) for key in input_array]) + 8
            file.write('{: <{l}}{:}\n'.format(key, val, l=max_len))
    return None


"""
# Задача_2
Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
"""


def create_txt_file(file_name: str) -> None:
    if os.path.exists(file_name):
        return print('File exists! Create new file.')
    with open(file_name, "w") as file:
        print('Write something to your file: ')
        while True:
            user_input = input()
            if user_input == '':
                break
            file.writelines(user_input + '\n')
    return None


if __name__ == '__main__':
    import_file = 'file.txt'
    export_file = 'average_points.txt'
    user_input_file = 'my_note.txt'
    create_file(average_points(import_file), export_file)
    print(min_points(average_points(import_file)))
    # create_txt_file(user_input_file)