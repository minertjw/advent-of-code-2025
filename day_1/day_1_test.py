from day_1.main import rotate


def test_1():
    position, zeros = rotate(50, "R49")
    assert position == 99
    assert zeros == 0


def test_2():
    position, zeros = rotate(50, "L49")
    assert position == 1
    assert zeros == 0


def test_3():
    position, zeros = rotate(0, "L100")
    assert position == 0
    assert zeros == 1


def test_4():
    position, zeros = rotate(0, "R100")
    assert position == 0
    assert zeros == 1


def test_5():
    position, zeros = rotate(1, "L50")
    assert position == 51
    assert zeros == 1
