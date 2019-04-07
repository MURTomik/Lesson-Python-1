# Практическое задание к уроку 4
print('Hello, Dmitriy!!!')
print('Практическое задание для урока 4')


# 1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

print('Задание 1')
def vivod_data(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name,age,city)

name = input('Введите имя:')
age = input('Введите возраст:')
city = input('Введите город проживания:')

print(vivod_data(name,age,city))

# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

#1 вариант
print('Задание 2 вариант 1')
def max_chislo(list):
    return  max(list)

i = 0
chislo_list = []
while i < 3:
    chislo_list.append(int(input('Введите число:')))
    i+=1

print(chislo_list)
print("Максимальное из них ", max_chislo(chislo_list))

print('Задание 2 вариант 2')
#2 вариант
def max_chislo(ch1,ch2,ch3):
    new_list=[ch1,ch2,ch3]
    print(new_list)
    return  max(new_list)

chislo1 = (int(input('Введите число:')))
chislo2 = (int(input('Введите число:')))
chislo3 = (int(input('Введите число:')))

print("Максимальное из них ", max_chislo(chislo1,chislo2,chislo3))



# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

print('Задание 3')
def attack(player,enemy):
    print('Данные на начало атаки:',player_dict)
    print('Данные на начало атаки:',enemy_dict)
    player_dict['health'] = player_dict['health'] - enemy_dict['damage']
    return player_dict, enemy_dict

name_player = input("Введите имя Игрока:")
name_enemy = input("Введите имя Противника:")

player_dict = {
    'name': name_player,
    'health':100,
    'damage':50
}
enemy_dict = {
    'name': name_enemy,
    'health':100,
    'damage':50
}
attack(player_dict,enemy_dict)

print('Данные после атаки:', player_dict)
print('Данные после атаки:', enemy_dict)


# 4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# 1. Наносит урон. Это улучшенная версия функции из задачи 3.
# 2. Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

print('Задание 4')
def attack(player,enemy):
    def armor_enemy(player1,enemy1):
        player1['damage']=round(player1['damage']/enemy1['armor'],2)
        enemy1['damage']=round(enemy1['damage']/player1['armor'],2)
        return player1['damage'],enemy1['damage']

    print('Данные на начало атаки:', player)
    print('Данные на начало атаки:', enemy)

    player.update({'armor':1.2})
    enemy.update({'armor':1.2})

    # print(player)
    # print(enemy)

    armor_enemy(player,enemy)

    print('Данные после урона:', player)
    print('Данные после урона:', enemy)

    player['health'] = player['health'] - enemy['damage']
    enemy['health'] = enemy['health'] - player['damage']
    return player,enemy


name_player = input("Введите имя Игрока:")
health_player = int(input("Введите здоровье Игрока:"))
damage_player = int(input("Введите броню Игрока:"))

name_enemy = input("Введите имя Противника:")
player_dict = {
    'name': name_player,
    'health': health_player,
    'damage': damage_player
}
enemy_dict = {
    'name': name_enemy,
    'health':100,
    'damage':50
}
while (True):
    attack(player_dict,enemy_dict)

    print('Данные после атаки:', player_dict)
    print('Данные после атаки:', enemy_dict)
    if player_dict['health']<=0:
        print("Вы проиграли")
        break
    elif enemy_dict['health']<=0:
        print("Ваш противник побежден!!!")
        break

    next_attak = int(input("Если хотите продолжить атаковать введите 1"))
    if next_attak != 1:
        break

