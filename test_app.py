from app import change


def test_change():
    assert [{5: 'quarters'}, {1: 'nickels'}, {4: 'pennies'}] == change(1.34)
    assert [{4: 'quarters'}] == change(1.0)