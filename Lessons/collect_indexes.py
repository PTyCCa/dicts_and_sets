"""Цель упражнения — функция collect_indexes(). Эта функция должна принимать на вход коллекцию (некий iterator/iterable) и возвращать словарь (или подобная ему коллекция!), где ключом будет элемент коллекции, а значением для ключа — список индексов коллекции, по которым встречается этот элемент."""

from collections import defaultdict


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result