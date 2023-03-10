# Задача 1. Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух 
# считает, что ритм есть, если число слогов (т.е. число гласных букв) в 
# каждой фразе стихотворения одинаковое. Фраза может состоять из одного 
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы
# отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в 
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с 
# ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# str = input("Введите фразу: ")
# str = str.split()
# sums = list()

# for s in str:
#     sums.append(sum(i in 'уеыаоэяию' for i in s))
# sums_set = set(sums)
# if len(sums_set) == 1 :
#     res = "Парам пам-пам"
# else:
#     res = "Пам парам"
# print(res)

phrase=input("Введите фразу: ").lower().split()
f = lambda x: sum(1 for i in x if i in "аеёиоуыэюя")
if all([f(i) == f(phrase[0]) for i in phrase]):
    print('Парам пам-пам')
else:
    print('Пам парам')