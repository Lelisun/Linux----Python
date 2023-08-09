
# Задание 1.
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае. # Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess

if __name__ == '__main__':

    # Вариант1.

    my_text = 'file.txt'
    result = subprocess.run('ls', shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    result_out = result.stdout
    print(result_out)
    if my_text in result_out and result.returncode == 0:
        print('True')
    else:
        print('Fail')

    # Вариант2.

    # def check_command_output(command, text):
    #     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    #     result_out = result.stdout
    #     print(result_out)
    #     if text in result_out and result.returncode == 0:
    #         print('True')
    #     else:
    #         print('Fail')
    #
    # command = "ls"
    # text = "file.txt"
    # result = check_command_output(command, text)



