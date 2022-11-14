from os import system
system('cls')


# 1) Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.

# lst = [1,2,34,-56, 33, 100, 7,8]
# f = filter(lambda x: abs(x % 10) and abs(x // 10), lst)
# for l in f:
#     print(*filter(lambda x: 9<abs(x)<100,lst))



# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# x = "12,sadf,5643"
# word =[]
# number = []
# for i in x:
#     if i.isalpha():
#         if not word or not last_isalpha:
#             word.append(i)
#         else:
#             word[-1] += i
#     else:
#         if not number or last_isalpha:
#             number.append(i)
#         else:
#             number[-1] += i
#     last_isalpha = i.isalpha()
# print(word, number,sep="\n")

# 3) Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# sum = 0
# input_num = input('Введите число: ')

# for a in input_num:
#     if a.isdigit():
#         sum += int(a)

# print(sum)

