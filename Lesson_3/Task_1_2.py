
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


# def trunslate(num):
#     trunslate_list = {'один':'one', 'два':'two', 'три':'three', 'четыри':'four', 'пять':'five', 'шесть':'six', 'семь':'seven', 'восемь':'eight', 'девять':'nine', 'десять':'ten'}
#     if num in trunslate_list:
#         return trunslate_list[num]
#     else:
#         return None


def trunslate(num):
    trunslate_list = {'один':'one', 'два':'two', 'три':'three', 'четыри':'four', 'пять':'five', 'шесть':'six', 'семь':'seven', 'восемь':'eight', 'девять':'nine', 'десять':'ten'}
    num_2 = num.lower()
    if num_2 in trunslate_list.keys():
        if num.istitle():
            return trunslate_list[num_2].capitalize()
        else:
            return trunslate_list[num_2]
    else:
        return None

print (trunslate('два'))



