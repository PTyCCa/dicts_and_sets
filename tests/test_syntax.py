from lessons.syntax import make_user, format_user

def test_make_user():
    bob = make_user('Bob', 42)
    assert len(bob) == 2
    assert 'name' in bob
    assert 'age' in bob
    assert bob['name'] == 'Bob'
    assert bob['age'] == 42


def test_format_user():
    assert format_user(solution.make_user('Joe', 30)) == 'Joe, 30'
    assert format_user(solution.make_user('Ann', 20)) == 'Ann, 20'
