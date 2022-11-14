from os import system
system ('cls')

# 1. Пользователь вводит число, Вам необходимо вывести число 
# Пи с той точностью знаков после запятой, сколько указал 
# пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

# import math
# from math import pi
# n = pi
# print(n)
# n = 100
# my_pi = sum(1 / 16 ** x * (4 / (8 * x + 1) - 2 / (8 * x + 4) - 1 / (8 * x + 5) - 1 / (8 * x + 6)) for x in range(n))
# print(my_pi)


# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

# import math
# def is_prime(n):
#     primes = [2]
#     for num in range(3, n + 1, 2):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
#             primes.append(num)
#     return primes
# def get_prime_factors(n, primes):
#     fact = []
#     for i in primes:
#         while n % i == 0:
#             n = n / i
#             fact.append(i)
#     return fact
# n = int(input('Введите число: '))
# primes = is_prime(n)
# factors = get_prime_factors(n, primes)
# print(factors)
# def testing(n, factors):
#     return math.prod(factors) == n       
# print(testing(n, factors))
# def task31 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)
# print (task31 (5))


# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# 3 1 2 3
# 2 1

# from random import randint
# def create_list(size, m, n):
#     return [randint(m, n) for i in range(size)]
# def get_unic_value(list):
#     return [i for i in set(list)]
# size = 10
# m = 1
# n = 10
# origin = create_list(size, m, n)
# print(origin)
# print(get_unic_value(origin))

# 4. Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) многочлена 
# и вывести многочлен степени k.


# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom1)

# Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios (k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('Polynomial2.txt', 'w') as data:
#     data.write(polynom2)



# *** 35. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


with open('Polynomial.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('Polynomial2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('Polynomial.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('Polynomial2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('Sum_Polynomial.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')




