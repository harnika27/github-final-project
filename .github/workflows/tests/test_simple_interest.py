def test_simple_interest():
    principal = 1000
    rate = 5
    time = 2

    interest = (principal * rate * time) / 100

    assert interest == 100
