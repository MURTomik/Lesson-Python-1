import json, pickle

with open('group1.pickle', 'rb') as f:
    pik_group = pickle.load(f)

print("Вывод из файла group1.pickle - ",pik_group)
print(type(pik_group)      )
print(pik_group['name'])
print(pik_group['tracks'])
print(pik_group['Albums'])
print('')


with open('group1.json', 'r') as f:
    js_group = json.load(f)

print("Вывод из файла group1.json - ",js_group)
print(type(js_group))

print(js_group['name'])
print(js_group['tracks'])
print(js_group['Albums'])