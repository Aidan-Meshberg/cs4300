import pytest
from task6 import wordCount

testFiles = ["task6_read_me.txt"]

#create test cases for each file using metaprogramming
for file in testFiles:
    def dynamicTest(file=file):
        expectedWordCount = 127
        result = wordCount(file)
        assert result == expectedWordCount, f"Expected {expectedWordCount} but got {result} for {file}"
    
    #set the dynamically generated function's name based on the file name
    dynamicTest.__name__ = f"testWordCount_{file.replace('.', '_')}"
    
    #set the dynamically created test function in pytest using globals()
    globals()[dynamicTest.__name__] = dynamicTest