def getAcronym(phrase):
    str_ = ''

    for i in phrase.split():
        str_ += i[0].upper()

    return str_
