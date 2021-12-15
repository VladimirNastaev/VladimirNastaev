### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration_time = int(input('Введите продолжительность времени:'))

do_day = duration_time // (60 * 60 * 24)
do_hour = duration_time - do_day * (60 * 60 * 24) // (60 * 60)
do_min = duration_time - do_day * (60 * 60 * 24) // do_hour * (60 * 60) // 60
do_second = duration_time - do_day * (60 * 60 * 24) // do_hour * (60 * 60) - do_min * 60
# print(do_day, 'дн', do_hour 'час', do_min, 'мин', do_second, 'сек')
print(do_day, 'дн', do_hour, 'час', do_min, 'мин', do_second, 'сек')


#до минуты:
# if duration_time <= do_min:
#     print('duration = ' + str(do_min) + ' сек')
# #до часа
# elif duration_time <= do_hour: #or duration_time >= do_hour:
#     print('duration = ' + str(do_hour) + ' сек')
# #до суток
# elif duration_time <= do_day:
#     print('duration = ' + str(do_day) + 'сек')