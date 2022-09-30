time = input('Укажите текущее время. Например: "01:10" ')
if time >= '8:00' and time <= '8:05':
    print("Подъём")
elif time >= '8:05' and time <= '8:10':
    print('Нужно выпить стакан воды')
elif time >= '8:10' and time <= '8:20':
    print('Сходить в туалет и почистить зубы')
elif time >= '8:20' and time <= '8:30':
    print('Небольшая разминка и медитация')
elif time >= '8:30' and time <= '9:00':
    print('Завтрак')
else:
    print('Неверные входные данные!')