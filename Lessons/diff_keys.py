"""В этом упражнении вам предстоит анализировать изменения, имея старую и новую версии словаря. Требуется реализовать функцию diff_keys(), которая должна принимать два словаря-аргумента — "старый" и "новый" — и возвращать словарь с результатами анализа. Результирующий словарь должен содержать строго три ниже перечисленных ключа:

'kept' — множество ключей, которые присутствовали в старом словаре и остались в новом;
'added' — множество ключей, которые отсутствовали в старом словаре, но появились в новом;
'removed' — множество ключей, которые присутствовали в старом словаре, но в новый не вошли."""

# BEGIN
def diff_keys(old, new):
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }
# END