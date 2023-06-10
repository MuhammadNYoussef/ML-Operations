from num_sqrt import square_num


def test_sqrt():
    assert square_num(2, 2) == 4
    assert square_num(3, 2) == 9
    assert square_num(5, 5) == 3125
