from bank import bankoper

def test_deposit():
    totalBalance, updateBalance = bankoper(200000,30000,0)

    assert totalBalance == 230000
    assert updateBalance == 2300000

def test_withdraw():
    totalBalance, updateBalance = bankoper(100000,40000,10000)

    assert totalBalance == 140000
    assert updateBalance == 130000

def test_anyamount():
    totalBalance, updateBalance = bankoper(150000, 0, 15000)

    assert totalBalance == 150000
    assert updateBalance == 135000
    

