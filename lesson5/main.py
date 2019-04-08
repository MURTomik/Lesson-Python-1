# 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

from code import my_module1
from code.my_module2_list import my_list

choice1 = int(input("Выберите номер (создать папку -1, удалить папку - 2, выбрать из списка - 3)"))

if choice1 == 1:
    my_module1.make_dir()
elif choice1 == 2:
    my_module1.remove_dir()
elif choice1 == 3:
    spisok = input('Введите список значений через запятую: ')
    print(my_list(spisok.split(',')))
else:
    print('Ввели не существующие действие')