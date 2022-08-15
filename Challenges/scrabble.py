"""Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра: набор символов (строку) и слово, и проверяет, можно ли из переданного набора составить это слово. В результате вызова функция возвращает True или False.

При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.

Для решения используйте встроенный инструмент — Counter."""

from collections import Counter


# BEGIN
def scrabble(string, word):
    letters = Counter(string.lower())
    for letter, count in Counter(word.lower()).items():
        if letters[letter] < count:
            return False
    return True

    # Можно было сделать ещё короче, если учесть то,
    # как работает вычитание для пары Counter!
    # Хватило бы: return not (Counter(word.lower()) - Counter(string.lower()))
# END