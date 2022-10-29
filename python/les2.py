# from distutils.file_util import write_file
from os import system
system ('cls')

# 1. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial, end=' ')


# 2. Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15:  Ответ: 3
# Для n = 35:  Ответ: 5

# n = int(input('Введите N: '))
# i = 2
# while i <= n:
#     if n%i == 0:
#         print(i)
#         break
#     i += 1


# 3. Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных 
# ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]


# n = int(input('Введите число '))
# list = []

# for i in range(-n,n+1):
#     list.append(i)
# print(list)

# res = 1
# with open('file.txt','w') as data:
#     data.write('2 \n')
#     data.write('1 \n')
#     data.write('3 \n')
#     data.write('0 \n')
#     data.write('5 \n')
#     # data.write('4 \n')

# patch = 'file.txt'
# data = open(patch, 'r')

# for line in data:
#     pos = int(line)
#     res *= list[pos]
# print(res)


# 4. Требуется посчитать сумму чётных чисел, 
# расположенных между числами 1 и N включительно.

a=int(input("Введите первое число = "))
b=int(input("Введите второе число = "))
ans = []
for i in range(a, b+1):
    if i%2==0:
        ans.append(i)
print(sum(ans))

