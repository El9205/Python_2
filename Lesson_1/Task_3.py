# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100

percent = 1
while percent <= 100:
    if str(percent)[len(str(percent))-1] == '1':
        print(percent, 'процент')
    elif str(percent)[len(str(percent))-1] == '2' or str(percent)[len(str(percent))-1] == '3' or str(percent)[len(str(percent))-1] == '4':
        print(percent, 'процента')
    elif str(percent)[len(str(percent))-1] == '5' or str(percent)[len(str(percent))-1] == '6' or str(percent)[len(str(percent))-1] == '7' or str(percent)[len(str(percent))-1] == '8' or str(percent)[len(str(percent))-1] == '9' or str(percent)[len(str(percent))-1] == '0':
        print(percent, 'процентов')
    percent = percent + 1