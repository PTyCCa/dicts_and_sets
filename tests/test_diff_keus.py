from Lessons.diff_keys import diff_keys


def test_diff_keys():
    old = {'x': 100, 'y': 200, 'z': 105}
    new = {'x': 100, 'y': 200, 'velocity': 2.5}
    diff = diff_keys(old, new)
    assert isinstance(diff, dict)
    assert set(diff.keys()) == {'added', 'removed', 'kept'}
    assert diff['kept'] == {'x', 'y'}
    assert diff['added'] == {'velocity'}
    assert diff['removed'] == {'z'}