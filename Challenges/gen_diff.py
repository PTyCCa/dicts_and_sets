"""Иногда в программировании возникает задача поиска разницы между двумя наборами данных, такими как словари. Например, при поиске различий в json файлах. Для этого даже существуют специальные сервисы, например, http://www.jsondiff.com/ (попробуйте нажать на ссылку sample data и затем кнопку Compare).

src/solution.py
Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает результат сравнения в виде словаря. Ключами результирующего словаря будут все ключи из двух входящих, а значением строка с описанием отличий: added, deleted, changed или unchanged.

Возможные значения:

added — ключ отсутствовал в первом словаре, но был добавлен во второй
deleted — ключ был в первом словаре, но отсутствует во втором
changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями
Пример работы:

from solution import gen_diff

>>> gen_diff(
...     {"one": "eon", "two": "two", "four": True},
...     {"two": "own", "zero": 4, "four": True},
... )
{"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
Подсказки
Фрагмент этой задачи разбирается в докладе "Ментальное программированиеhttps://www.youtube.com/watch?v=vkUTX1hruF8""""

# BEGIN
def gen_diff(data1, data2):
    keys = data1.keys() | data2.keys()  # https://youtu.be/vkUTX1hruF8?t=929
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result
# END