# 1. Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

my_list = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
print(my_list)
for i in my_list:
    if isinstance(i, int):
        print ('Тип данных - int')
    elif isinstance(i, str):
        print ('Тип данных - srt')
    elif isinstance(i, float):
        print ('Тип данных - float')
    else:
        print('Щто ты такое?! О_О')


# некрасивый экспресс вариант
# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))