#boilerplate to just open file and split text
def wordCount(fileName):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    words = text.split()  # Cutting spaces to get words
    return len(words)