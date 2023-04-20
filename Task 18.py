# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

list_1 = []
n= int (input("Введите число: "))
x = int (input('введите X: '))
for i in range (n):
    list_1.append(randint (1,n))
    if abs(list_1[i-1]-list_1[i]) < 2 and list_1[i] == x:
        resalt = list_1[i-1]
    else:
        print ('нет такого числа')
    
print (list_1)
print(resalt)
# list_A = []
# difference_X = 100
# search_number = -1

# for i in range(n):
#     list_A.append(randint(1,n))
#     if abs(list_A[i]- X)< difference_X:
#         difference_X = abs(list_A[i]- X)
#         search_number = list_A[i]
# print(list_A)
# print("->",search_number)