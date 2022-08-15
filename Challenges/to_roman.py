"""Для записи цифр римляне использовали буквы латинского алфавита: I, V, X, L, C, D, M. Например:

1 обозначалась с помощью буквы I
10 с помощью Х
7 с помощью VII
Число 2020 в римской записи — это MMXX (2000 = MM, 20 = XX).

'src/solution.py'
Реализуйте функцию to_roman(), которая переводит арабские числа в римские. Функция принимает на вход целое число из диапазона от 1 до 3000, а возвращает строку с римским представлением этого числа.

Реализуйте функцию to_arabic(), которая переводит число в римской записи в число, записанное арабскими цифрами. Если переданное римское число не корректно, то функция должна вернуть значение False."""

NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


# BEGIN

def descending(pair):
    return -pair[1]


def to_roman(number):
    result = ''
    for roman, arabic in sorted(NUMERALS.items(), key=descending):
        repetitions_count = number // arabic
        number -= arabic * repetitions_count
        result += roman * repetitions_count
    return result


def to_arabic(number):  # noqa: WPS210
    numbers = []
    for char in number:
        numbers.append(NUMERALS[char])
    # Сдвиг чисел с повтором последнего
    # Пример: [1,2,3,4] -> [2,3,4,4]
    shifted_numbers = numbers[1:] + numbers[-1:]
    result = 0
    for previous, current in zip(numbers, shifted_numbers):
        if previous >= current:
            result += previous
        else:
            result -= previous
    if to_roman(result) != number:
        return False
    return result
# END