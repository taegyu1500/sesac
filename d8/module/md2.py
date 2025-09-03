from calc import power, square_root, is_number

def test_operation():
    print(power(2, 3))  # 8
    print(square_root(16))  # 4
    print(is_number("123"))  # True
    print(is_number("abc"))  # False
    
test_operation()