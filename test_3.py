import task3

def testCheckNumber():
    assert task3.checkNum(10) == "Pos num"
    assert task3.checkNum(-5) == "Neg num"
    assert task3.checkNum(0) == "Num is 0"

def testFirstTenPrimes():
    assert task3.firstTenPrimes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def testSumNums():
    assert task3.sumNums() == 5050
