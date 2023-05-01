from calculator import square


def main():
    test_square()


# It gives the AssertionError for not following the assertion keyword


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 Squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 Squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 Squared was not 0")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 Squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 Squared was not 9")


if __name__ == "__main__":
    main()
