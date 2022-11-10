from os import system
system('cls')

# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Вариант человек против человека
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# Вариант человек против БОТА

# import random
# from random import randint, choice

# messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
#             'сколько конфет берем?', 'берите еще', 'Ваш ход']
# max_number_move = 0
 
# def introduce_players():
#     player1 = input('Игрок №1, представьтесь пожалуйста\n')
#     player2 = 'BOTintelect'
#     print(f'Очень приятно, сегодня Вы играете с {player2}')
#     return [player1, player2]
 
# def sweets_game(players):
#     global max_number_move
#     total_sweets = int(input('Введите cколько всего конфет на кону:\n'))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_smart_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Я BOTintelect забираю {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Я BOTintelect забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
 
 
# players = introduce_players()
# sweets = sweets_game(players)
 
# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')



# 2) Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)




# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

with open('RLE.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

with open('RLE2.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)