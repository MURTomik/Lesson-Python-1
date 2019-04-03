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
            vivod = 'кг, предлагаем стать лицом нашего медицинского учреждения !'

        print('Пациенту,',surname,name,', возраст',age,'лет,','вес',weight,vivod)

    elif num_work == 4:
        # Задание №4
        print('Задания кончились')

    elif num_work == 5:
        # Задание №5
        print('Задания кончились')

    elif num_work == 6:
        # Задание №6
        print('Задания кончились')

    elif num_work == 0:
        break
    else:
        break

    next = int(input('Хотите продолжить введите 1'))
    if next != 1:
       break
