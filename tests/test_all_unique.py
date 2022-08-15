from Lessons.all_unique import all_unique


def test_all_unique():
    assert all_unique(iter([])), "Should work with iterators."
    assert all_unique(iter([1])), (
        "Should handle non-restartable iterators too."
    )
    assert all_unique([])
    assert all_unique("cat")
    assert not all_unique("lol")