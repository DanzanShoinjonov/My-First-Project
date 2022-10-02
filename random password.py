import random
#добавление констант 
digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUCWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''     #пустая переменная
#запрос имени
print('Добрый день, как вас зовут?')
name = input()
print('Добро пожаловать,', name,',в случайный генератор паролей.\nЗдесь вы можете создать случайный пароль, соответсвующий вашим критериям.')

#характеристика пароля/ей (входные данные)
print('Сколько паролей вам нужно?')
kol_vo = int(input())
print('Длина одного пароля должна быть ...')
long_s = int(input())
print('Включать ли цифры "1234567890"? (д - да, н - нет)')
nums = input()
print('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (д - да, н - нет)')
propisn_b = input()
print('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? (д - да, н - нет)')
stroch_b = input()
print('Включать ли символы "!#$%&*+-=?@^_"? (д - да, н - нет)')
simvols = input()
print('Исключать ли неоднозначные символы "il1Lo0O"? (д - да, н - нет)')
neodnazn_s = input()

#входные данные, которые изменяют переменную "chars"
if nums.lower() == 'д':
    chars += digits
if propisn_b.lower() == 'д':
    chars += uppercase_letters
if stroch_b.lower() == 'д':
    chars += lowercase_letters
if simvols.lower() == 'д':
    chars += punctuation
if neodnazn_s.lower() == 'д':
    for c in 'il1Lo0O':
        chars.replace(c, '')

#основная функция
def random_pass(long_s, chars):
    password = ''
    for j in range(long_s): #цикл с длиной пароля, без него нижняя строка выдала бы только один символ
        password += random.choice(chars)
    print(password)

#сколько паролей нужно пользователю, если "kol-vo", к примеру 2, до цикл сработает два раза, соответсвенно функция выдаст 2 пароля
for _ in range(kol_vo):
    random_pass(long_s, chars)
