# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

list_1 = []
n= int (input("Введите число: "))
for i in range (n):
    list_1.append(randint (1,n))
   
print (list_1)
    
# N = int(input("Введите число: "))
X = int (input('введите X: '))
# list_1 = list(range(1, N+1))
count_X = 0
for i in range(n):
    if list_1[i]== X:
        count_X +=1
print(list_1)
print(count_X)