import os
import shutil

# print(os.getcwd())
print(os.listdir())
print(os.listdir('/home/tarchanskyj/projects/personal'))
print(os.listdir('homeworks'))

# os.mkdir('test_dir')
# os.mkdir('test')
# os.mkdir('test/test_dir')
# os.makedirs('test/test_dir', exist_ok=True)

# os.remove('test_dir')
# shutil.rmtree('test')

# os.rename('test/test_dir', 'testt')

# os.path.join()
# print(os.path.dirname(os.getcwd()))
# print(os.path.isdir('testt'))
# print(os.path.isfile('testt'))
#
# print(os.path.split('test/dfdssf/text.txt'))
# print(os.path.splitext('test/dfdssf/text.txt'))

#
# def create_dir(dir_path: str, test_arg: bool = False) -> None:
#     try:
#         # 8 / 0
#         os.mkdir(dir_path)
#         print('Directory created')
#     # except:
#     except FileExistsError:
#         print('Directory exists')
#     except ZeroDivisionError:
#         print('ZeroDivisionError ERROR')
#
# create_dir('test/test10')
# # os.mkdir('test1')
#
#
# def create_dir_2(dir_path: str) -> None:
#     if os.path.isdir(dir_path):
#         print('Directory exists')
#     else:
#         os.mkdir(dir_path)
#         print('Directory created')
#
# create_dir_2('test/test101')
#
#
# try:
#     int(value)
# except:
#     print('We need int')
