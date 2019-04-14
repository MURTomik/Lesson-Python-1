# 1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['яблоко','банан','виноград','личи','слива','алыча']
fruits2 = ['апельсин','алыча','слива','банан','киви','яблоко','груша']

rezult_fruit = []
for fruit1 in fruits1:
    for fruit2 in fruits2:
        if fruit1 == fruit2:
            rezult_fruit.append(fruit1)
            break
print("Результат классическим способом: ",rezult_fruit)

#rezult_fruit1 = [fruit1 for fruit1 in fruits1 if fruit1 == [fruit2 for fruit2 in fruits2 if fruit2 != '']]
rezult_fruit = [fruit1 for fruit1 in fruits1 for fruit2 in fruits2 if fruit1 == fruit2]
print("Результат через генератор: ",rezult_fruit)

