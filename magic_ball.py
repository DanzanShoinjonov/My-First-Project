import random

print('Итак, вы стоите напротив черного-магического шара, внутри которого находится "икосаэдр"...')
print('Вы хотите взболтать и спросить о чём-нибудь шар? (д - да, н - нет)')

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да',
'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее - всего', 'Хорошие перспективы',
'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спороси опять',
'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

again = 'д'


def is_valid():
    r = input()
    if r == 'д':
        magic_random()
    if r != 'д' and r != 'н':
        print('Пожалуйста, проверьте, что написали. (д - да, н - нет)')
        is_valid()
    if r == 'н':
        print('Надеюсь, что мы ещё увидимся!:)')



def magic_random():

    print('Вы начинаете вращать шар... Я предсказываю ваше будещее...')
    #print('Вы подумали, о том, что хотите спросить?')
    return print(random.choice(answers))



is_valid()
