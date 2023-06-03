from num_sqrt import square_num

def test_1():
    assert square_num(2, 2) == 4
    
def test_2():
    assert square_num(3, 2) == 9

def test_3():
    assert square_num(5, 5) == 3125
