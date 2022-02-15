import os


def get_files_from_dir(base_dir: str, full_path: bool = True) -> list:
    if not os.path.isdir(base_dir):
        print('No such dir!')
        return []
    list_dir = os.listdir(base_dir)
    if full_path:
        list_dir = [os.path.join(base_dir, name) for name in list_dir]
    return list_dir


# print(get_files_from_dir('test'))
# print(get_files_from_dir('test', full_path=False))


# file_obj = open('names.txt', 'r')
# print(file_obj)
# # data = file_obj.read()
# data = file_obj.read(10)
# print(data)
# print(data.split('\n'))
# file_obj.seek(0)
# data = file_obj.read(10)
# print(data)
#
# file_obj.close()
# data = file_obj.read(10)
# print(data)
'''

Режим	Обозначение
'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x'	открытие на запись, если файла не существует, иначе исключение.
'a'	открытие на дозапись, информация добавляется в конец файла.
'b'	открытие в двоичном режиме.
't'	открытие в текстовом режиме (является значением по умолчанию).
'+'	открытие на чтение и запись

'''
#
# with open('names.txt', 'r') as file_obj:
#     # data = file_obj.read()
#     # data = file_obj.readlines()
#     data = [row for row in file_obj]
# print(data)
#
#
# with open('names_2.txt', 'w') as file_obj:
#     # file_obj.write('Hello\nHello')
#     file_obj.writelines(['Hello\n', 'Hello\n', '2'])
#
