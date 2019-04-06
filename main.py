# Практическое задание к уроку 2

print('Hello, Dmitriy!!!')
print('Практическое задание для урока 2')

while (True):
    print(' ')
    num_work = int(input('Введите номер задания (выход - 0): '))

    if num_work == 1:
        # Задание №1
        print(' ')
        print('Задание №1')
        chislo = int(input('Введите число: '))
        #print(type(chislo))
        chislo += 2
        #print(type(chislo))
        print('Результат:', chislo)

    elif num_work == 2:
        # Задание №2
        print(' ')
        print('Задание №2')
        while (True):
            chislo = int(input('Введите число больше 0, но меньше 10: '))
            #цикл
            if 0 < chislo < 10:
                print('Поздравляю, Вы ввели верное число и выиграли', chislo ** 2, 'млн.руб.')
                break
            else:
                print('Задание не читаем!!!')

#####
    elif num_work == 3:
        # Задание №3
        print(' ')
        print('Задание №3 Медицинская карта')
        surname = input('Введите Фамилию: ')
        name = input('Введите Имя: ')
        age = int(input('Введите Возраст: '))
        weight = int(input('Введите Вес: '))
        print(' ')
        if age < 30 and (weight >= 50 or weight <= 120):
            vivod = 'кг, Вы в хорошем состоянии !'
        elif age > 40 and (weight < 50 or weight > 120):
            vivod = 'кг, требуется врачебный осмотр !'
        elif age > 30 and (weight < 50 or weight > 120):
            vivod = 'кг, требуется заняться собой !'
        elif (age == 30 or age == 40) and (weight < 50 or weight > 120):
            vivod = 'кг, срочно улучшить показатели по весу !'
        else:
            vivod = 'кг, предлагаем Вам стать лицом нашего медицинского учреждения !'
        print('Пациент,{} {}, возраст {} лет, вес {} {}'.format(surname,name,age,weight,vivod))

    elif num_work == 4:
        # Задание №4
        print(' ')
        print('Задание №4')
        spisok1 = input('Введите первый список значений через запятую: ')
        spisok2 = input('Введите второй список значений через запятую: ')
        spisok1 = spisok1.split(',')
        spisok2 = spisok2.split(',')
        print(spisok1, spisok2)
        spisok = set(spisok1) - set(spisok2)
        print(list(spisok))

    elif num_work == 5:
        # Задание №5
        print(' ')
        print('Задание №5')
        while (True):
            date_chislo = input('Введите дату: ')
            date_chislo = date_chislo.split('.')
            month = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
            print(date_chislo)
#            print(date_chislo[1])
            if len(date_chislo) == 3:
                if 0 < int(date_chislo[1]) < 13:
                    print('Дата: {} {} {} года'.format(date_chislo[0],month[int(date_chislo[1])-1],date_chislo[2]))
                    break
                else:
                    print('Дата неверная')
            else:
                print('Дата неверная')
    elif num_work == 6:
        # Задание №6
        print(' ')
        print('Задание №6')
        spisok1 = input('Введите список значений через запятую: ')
        #spisok2 = input('Введите список2 через запятую: ')
        spisok1 = spisok1.split(',')
        #spisok2 = spisok2.split(',')
        print(spisok1)
        spisok = set(spisok1)
        #print(spisok)
        print(list(spisok))
        #- set(spisok2))

#    elif num_work == 0:
#       break
    else:
        break

    next = int(input('Хотите продолжить введите 1'))
    if next != 1:
       break
