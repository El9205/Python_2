# 1. Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input ('Введите количество секунд: '))
while duration < 0:
    duration = int(input('Ну уж нет, попробуй еще раз: '))
if duration // 60 == 0:
    print(duration, ' сек')
elif duration // 60 > 0 and duration // 3600 == 0:
    print(duration // 60, 'мин', duration % 60, ' сек')
elif duration // 3600 > 0 and duration // 86400 == 0:
    print(duration // 3600, 'час', (duration % 3600)//60, 'мин', (duration % 3600) % 60, 'сек')
elif duration // 86400 > 0:
    print(duration // 86400, 'дн', (duration % 86400) // 3600, 'час', ((duration % 86400) % 3600) // 60, 'мин', ((duration % 86400) % 3600) % 60, 'сек')