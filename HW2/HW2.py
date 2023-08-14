# Добавить в проект тесты, проверяющие работу команд
# d (удаление из архива) и u (обновление архива). Вынести
# в отдельные переменные пути к папкам с файлами, с архивом
# и с распакованными файлами. Выполнить тесты с ключом -v.
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

import subprocess

folder_in = '/home/user/seminar/tst'
folder_out = '/home/user/seminar/out'
folder_ext = '/home/user/seminar/extract'


def checkout(cmd, text):

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

print(checkout(f'cd {folder_in}; 7z a {folder_out}/arh1', 'Everything is Ok'))


def test_step1():
    assert checkout(f'cd {folder_in}; 7z a {folder_out}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {folder_in}; 7z d {folder_out}/arh1.7z', 'Everything is Ok'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folder_in}; 7z u {folder_out}/arh1', 'Everything is Ok'), 'test3 FAIL'


def test_step4():
    assert checkout(f'cd {folder_out}; 7z l arh1.7z', 'test1.txt'), 'test4 FAIL'


def test_step5():
    assert checkout(f'cd {folder_out}; 7z x arh1.7z -o{folder_ext} -y', 'Everything is Ok'), 'test5 FAIL'

