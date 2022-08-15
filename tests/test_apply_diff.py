from Lessons.apply_diff import apply_diff

A, B, C, D = 'abcd'


def test_empty_result():
    assert apply_diff(set(), {}) is None, "Function should not return anything!"


def test_apply_no_dict_mutating():
    original_diff = {'remove': {A}}
    diff = original_diff.copy()
    apply_diff({B}, diff)
    assert diff == original_diff, "Function should not touch the dictionary!"


def test_apply_empty_diff():
    target = {A, B, C}
    apply_diff(target, {})
    assert target == {A, B, C}, "Empty diff should not change anything!"


def test_apply_unrelated_dict():
    target = {A, B}
    apply_diff(target, {'foo': 'bar', True: False})
    assert target == {A, B}, "Unrelated keys should not affect target!"


def test_apply_empty_sets():
    target = {A, B, C}
    apply_diff(target, {'add': set(), 'remove': set()})
    assert target == {A, B, C}, "Empty sets should not affect target!"


def test_apply_addition():
    target = {A, B, C}
    apply_diff(target, {'add': {C, D}})
    assert target == {A, B, C, D}


def test_apply_rejecting():
    target = {A, B, C}
    apply_diff(target, {'remove': {A, B}})
    assert target == {C}