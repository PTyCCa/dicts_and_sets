from Lessons.toggle import toggle, toggled


def test_toggle():
    a, b = "ab"
    flags = set()
    result = toggle(a, flags)
    assert result is None, "Should not return anything!"
    assert flags == {a}
    toggle(b, flags)
    assert flags == {a, b}
    toggle(a, flags)
    assert flags == {b}
    toggle(b, flags)
    assert not flags


def test_toggle_ints():
    a, b = (42, 100)
    flags = set()
    result = toggle(a, flags)
    assert result is None, "Should not return anything!"
    assert flags == {a}
    toggle(b, flags)
    assert flags == {a, b}
    toggle(a, flags)
    assert flags == {b}
    toggle(b, flags)
    assert not flags


def test_toggled():
    a, b, c = "abc"
    flags = {a, b}
    assert toggled(c, flags) is not flags, "Should return a new set!"
    assert flags == {a, b}, "Old set should not be changed!"
    assert c in toggled(c, flags)
    assert b not in toggled(b, flags)


def test_roundtrip_toggle():
    a, b, c = "abc"
    flags = {a, b}
    toggle(c, flags)
    toggle(c, flags)
    assert flags == {a, b}


def test_roundtrip_toggled():
    a, b, c = 1, 2, 3
    flags = {a, b}
    assert toggled(c, toggled(c, flags)) == flags