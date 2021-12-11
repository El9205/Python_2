# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# a. Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.

num = 1
cube_list = []
while num <= 1000:
    if num % 2 != 0:
        cube_list.append(str(num**3))
    num = num + 1
print(cube_list)


# a
counter_list = 0
counter_element = 0
list_sum = 0
element_sum = 0
while counter_list < len(cube_list):
    counter_element = 0
    element_sum = 0
    element = 0
    while counter_element < int(len(cube_list[counter_list])):
        element_sum = element_sum + int(cube_list[counter_list][counter_element])

        counter_element = counter_element + 1
    if element_sum % 7 == 0:
        list_sum = list_sum + int(cube_list[counter_list])
    counter_list = counter_list + 1
print(list_sum)


# b
for i in cube_list:
    i = int(i) + 17
    print('i', i)
    while counter_list < len(cube_list):
        counter_element = 0
        element_sum = 0
        element = 0
        while counter_element < int(len(cube_list[counter_list])):
            element_sum = element_sum + int(cube_list[counter_list][counter_element])

            counter_element = counter_element + 1
        if element_sum % 7 == 0:
            list_sum = list_sum + int(cube_list[counter_list])
        counter_list = counter_list + 1
    print(list_sum)