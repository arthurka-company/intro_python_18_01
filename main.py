def user_info():
    while True:
        res = input('Введите текст: ')
        with open('input.txt', 'a') as new_file:
            new_file.writelines(res + '\n')
        if not res:
            break
    return


user_info()