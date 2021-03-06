# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

prices = [57.8, 46.51, 97, 0.01, 50, 96.1, 450, 8.3, 5, 68, 1.52, 19, 2.3, 4.06, 37]

print(id(prices))
for i in prices:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

prices.sort()
for i in prices:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

print(id(prices))
new_prices = sorted(prices)[::-1]
print(new_prices)
for i in new_prices[:5]:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')
