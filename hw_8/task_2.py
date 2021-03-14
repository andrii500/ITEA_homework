def getDividers(n):
    list_ = []

    for i in range(1, n + 1):
        if n % i == 0:
            list_.append(i)

    return list_
