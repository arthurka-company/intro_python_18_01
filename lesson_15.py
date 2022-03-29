# CLI - command line interface
# python3 script_name.py dir_name value
# python3 script_name.py -value=dir_name
# python3 script_name.py --d dir_name
# pip install requests --url_index https://....

# import sys
#
#
# if __name__ == '__main__':
#     print(sys.argv)
#
#     if len(sys.argv) != 3:
#         # raise AttributeError('Script need two argments!')
#         print('Script need two argments!')
#         sys.exit()
#
#     if any([not i.isdigit() for i in sys.argv[1:]]):
#         raise ValueError('Args must be int!!!')
#
#     # assert sys.argv[2] in ['r', 'w', 'bw']
#
#     arg_1 = sys.argv[1]
#     arg_2 = sys.argv[2]
#
#     print(int(arg_1) + int(arg_2))

# import argparse
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Script for sum!')
#     parser.add_argument('value_1', type=int, help='First argument for sum')
#     parser.add_argument('--value_2', type=int, help='First argument for sum')
#     parser.add_argument('--value_3', type=int, help='First argument for sum')
#     args = parser.parse_args()
#
#     print(args)
#     print(args.value_1 + args.value_2)
