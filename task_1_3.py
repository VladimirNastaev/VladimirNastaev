# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

percent = int(input('Введите число процента: '))
if percent == 1:
    word = 'процент'
elif percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)