def add(x, y):
    return x + y


def test_add_when_one_and_two_expect_three():
    # Arrange:
    expected = 3

    # Act:
    actual_result = add(1, 2)

    # Assert:
    if actual_result == expected:
        print('OK')
    else:
        print('WRONG!')


def test_add_when_two_and_one_expect_three():
    expected = 3
    actual_result = add(2, 1)
    if actual_result == expected:
        print('OK')
    else:
        print('WRONG!')


def test_add_when_five_and_minus_five_expect_zero():
    expected = 0
    actual_result = add(5, -5)
    if actual_result == expected:
        print('OK')
    else:
        print('WRONG!')


def test_add_when_none_and_two_expect_exception():
    expected = 0
    actual_result = add(None, 1)
    if actual_result == expected:
        print('OK')
    else:
        print('WRONG!')


# test_add_when_none_and_two_expect_exception()
# test_add_when_one_and_two_expect_three()
# test_add_when_two_and_one_expect_three()
# test_add_when_five_and_minus_five_expect_three()
