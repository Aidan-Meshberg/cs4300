import task4

def testCalcDiscountIntInt():
    assert task4.calcDiscount(100, 20) == 80

def testCalcDiscountFloatInt():
    assert task4.calcDiscount(100.0, 20) == 80.0

def testCalcDiscountIntFloat():
    assert task4.calcDiscount(100, 10.5) == 89.5

def testCalcDiscountFloatFloat():
    assert task4.calcDiscount(100.0, 10.5) == 89.5