from Lessons.count_all import count_all


def test_count_all():
    assert count_all([]) == {}
    assert count_all("") == {}
    assert len(count_all("cat")) == 3
    assert len(count_all("foo")) == 2
    assert list(count_all("dog").values()) == [1, 1, 1]
    assert count_all("ololo")["o"] == 3