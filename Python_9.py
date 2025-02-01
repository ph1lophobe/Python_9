import random
import time
from json.encoder import encode_basestring

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
en_chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
            'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
en_upper_chars = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                  'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L','Z', 'X',
                  'C', 'V', 'B', 'N', 'M']
chars = [':', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', ',', '~',
         '{', '}', '[', ']', '<', '>', '?', '.', ';', '#', '№', '|', '/', '`']

allCharsForUser = []
numbersCount = 0
enCount = 0
enUppCount = 0
charsCount = 0

print('Введите пароль для анализа:')
userPassword = input('Ваш пароль: ')
countPassword = len(userPassword)
print(f'В вашем пароле {countPassword} символов')

for char in list(userPassword):
    if char in numbers:
        numbersCount += 1
    if char in en_chars:
        enCount += 1
    if char in en_upper_chars:
        enUppCount += 1
    if char in chars:
        charsCount += 1

hard = 0
print('Ваш пароль содержит:')
if numbersCount > 0:
    print('Цифры: ', numbersCount)
    hard += 1
    allCharsForUser += numbers
if enCount > 0:
    print('Латинские маленькие символы: ', enCount)
    hard += 1
    allCharsForUser += en_chars
if enUppCount > 0:
    print('Латинские большие символы: ', enUppCount)
    hard += 1
    allCharsForUser += en_upper_chars
if charsCount > 0:
    print('Символы: ', charsCount)
    hard += 1
    allCharsForUser += chars

if countPassword > 8:
    hard += 1
if hard <= 5:
    print('Ваш пароль достаточно сильный!')
elif hard <= 3:
    print('Ваш пароль средний!')
else:
    print('Ваш пароль очень слабый, его нужно поменять(')

repatCount = 0

res = input('Начать попытку перебора пароля? (да | нет): ')
if res.lower() == 'да':
    start_time = time.time()
    newPass = ''
    while newPass != userPassword:
        repatCount += 1
        newPass = ''

        for i in range(countPassword):
            newPass += random.choice(allCharsForUser)
        print(newPass)

    end_time = time.time()
    print('Попыток потребовалось: ', repatCount)
    elapsed_time = end_time - start_time
    print(f'Затраченное время: {round(elapsed_time, 2)} секунд')