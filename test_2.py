import task2

def testInteger():
    assert task2.intVal == 10

def testFloat():
    assert task2.floatVal == 5.5

def testString():
    assert task2.stringVal == "a string"

def testBoolean():
    assert task2.boolVal is True #using literal, usually works better for bool's