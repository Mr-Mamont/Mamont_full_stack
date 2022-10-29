from os import system
system ('cls')

# 1. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# from random import randint
# import math
# def get_numbers(n, frst, last):
#     return [randint(frst, last) for i in range(n)]
# def mult_pairs(my_list):
#     return [my_list[i] * my_list[-i - 1] for i in range(math.ceil(len(my_list)/2))]
# n = 9
# frst = 1
# last = 10
# my_list = get_numbers(n, frst, last)
# print(my_list)
# print(mult_pairs(my_list))

# 2. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform
# def get_real_nums (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]
# def find_diff(my_nums):
#     nums = [round(x - int(x), 2) for x in (my_nums)]
#     return max(nums) - min(nums)
# n = 5
# frst = 1
# last = 10
# my_nums = get_real_nums(n, frst, last)
# print (my_nums)
# print(find_diff(my_nums))

# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите десятичное число: '))
# def conv_dec_to_bin(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]
# print(conv_dec_to_bin(n))



# 4. Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

n = int(input('Введите число: '))
def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums
fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))
