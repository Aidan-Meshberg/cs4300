import task5

def testFavoriteBooks():
    assert task5.firstThreeBooks == [
    {"title": "One Piece", "author": "Eiichiro Oda"},
    {"title": "Fullmetal Alchemist: Brotherhood", "author": "Hiromu Arakawa"},
    {"title": "Maximum Ride", "author": "James Patterson"}
    ]

def testStudentDatabase():
    assert task5.studentDatabase == {
        "Aidan Meshberg": 11748,
        "John Doe": 46290,
        "Jane Smith": 80081
    }
