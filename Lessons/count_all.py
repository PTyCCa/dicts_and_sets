"""Цель упражнения — функция count_all. Эта функция должна принимать на вход iterable источник и возвращать словарь, ключами которого являются элементы источника, а значения отражают количество повторов элемента в коллекции-источнике. Вот пара примеров, демонстрирующих то, как функция должна работать:"""


# BEGIN
def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters
# END