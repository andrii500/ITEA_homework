import re


def createModFile(path):
    inputFile = open(path, 'r')
    outputFile = open('outputHw8.txt', 'w')

    for line in inputFile:
        line = line.replace('\n', '')
        str_ = ''

        letters = list(filter(None, re.split('\d+', line)))
        digits = list(filter(None, re.split('[a-zA-Z]+', line)))

        for i in range(len(letters)):
            str_ += letters[i] * int(digits[i])

        outputFile.write(str_ + '\n')

    inputFile.close()
    outputFile.close()
