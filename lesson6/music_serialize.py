# 1. Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import json, pickle
import os

if os.path.exists("group1.pickle") == True:
    os.remove('group1.pickle')
if os.path.exists("group2.pickle") == True:
    os.remove('group2.pickle')
if os.path.exists("group1.json") == True:
    os.remove('group1.json')
if os.path.exists("group2.json") == True:
    os.remove('group2.json')


my_favourite_group = {
'name': 'The Rasmus',
'tracks': ['October & April (Октябрь и апрель)', 'Sail Away (Отправляюсь в путь)'],
'Albums': [{'name': 'Best of 2001-2009','year': 2009},
{'name': 'Hide from the Sun','year': 2005}]}

pik_group = pickle.dumps(my_favourite_group)
js_group = json.dumps(my_favourite_group)

print(pik_group)
print(type(pik_group))
print(js_group)
print(type(js_group))
#---
with open('group1.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('group2.pickle', 'wb') as f:
    pickle.dump(pik_group, f)

# эксперименты с переменной json.dump(json.loads(js_group),f)

with open('group1.json', 'w', encoding = 'utf-8') as f:
#with open('group1.json', 'w') as f:
    json.dump(my_favourite_group,f)

with open('group2.json', 'w') as f:
    json.dump(json.loads(js_group),f)
#---
# with open('group1.json', 'r', encoding = 'utf-8') as f:
# #with open('group1.json', 'r') as f:
#     print("1 - ",json.load(f))
#
# with open('group2.json', 'r') as f:
#     print("2 - ",json.load(f))

print("The end.")