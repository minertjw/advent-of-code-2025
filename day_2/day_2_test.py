from day_2.main import check_range


def test_1():
    invalid_ids = check_range("11-22")
    assert len(invalid_ids) == 2
    assert invalid_ids[0] == 11
    assert invalid_ids[1] == 22


def test_2():
    invalid_ids = check_range("95-115")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 99


def test_3():
    invalid_ids = check_range("998-1012")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 1010


def test_4():
    invalid_ids = check_range("1188511880-1188511890")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 1188511885


def test_5():
    invalid_ids = check_range("222220-222224")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 222222


def test_6():
    invalid_ids = check_range("1698522-1698528")
    assert len(invalid_ids) == 0


def test_7():
    invalid_ids = check_range("446443-446449")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 446446


def test_8():
    invalid_ids = check_range("38593856-38593862")
    assert len(invalid_ids) == 1
    assert invalid_ids[0] == 38593859

def test_9():
    invalid_ids = check_range('9226466333-9226692707')
    assert len(invalid_ids) == 3
    assert invalid_ids[0] == 9226492264
    assert invalid_ids[1] == 9226592265
    assert invalid_ids[2] == 9226692266
