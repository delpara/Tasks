# Вывод времени
duration = int(input('Введите число: '))
if duration < 60:
    print(duration, 'сек')
elif duration <= 3600:
    print(duration // 60, 'мин', duration % 60, 'сек')
elif 3600 < duration <= 86400:
    h = duration // 3600
    m = (duration - (h * 3600)) // 60
    s = (duration - h * 60) % 60
    print(h, 'час', m, 'мин', s, 'сек')
elif duration > 86400:
    d = duration // 86400
    h = (duration - (d* 86400)) // 3600
    m = (duration - (d * 86400) - (h * 3600)) // 60
    s = (duration - 86400 - (h * 3600)) % 60
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
