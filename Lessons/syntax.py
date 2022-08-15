"""В этой практике вам нужно реализовать две функции:

функцию make_user(), которая должна принимать два параметра — имя пользователя и возраст (число). Вернуть функция должна словарь с ключами 'name' и 'age', по которым должны быть сохранены соответствующие значения.
функцию format_user(), которая, будучи применена к результату вызова make_user() (помним — это словарь), должна вернуть строку вида 'Phil, 25'."""

# BEGIN
def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(user):
    return '{}, {}'.format(user["name"], user["age"])
# END