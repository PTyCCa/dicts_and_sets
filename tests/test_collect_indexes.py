from Lessons.collect_indexes import collect_indexes


def test_collect_indexes():
    assert not collect_indexes([])
    assert collect_indexes([1]) == {1: [0]}
    assert collect_indexes([1, 2]) == {1: [0], 2: [1]}  # noqa: WPS200
    assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
    assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}  # noqa: WPS221
